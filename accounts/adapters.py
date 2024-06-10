from base64 import b64encode
from concurrent.futures import ThreadPoolExecutor
from typing import Union
from urllib.parse import urlencode

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.forms import ResetPasswordForm
from allauth.account.models import EmailAddress
from allauth.account.utils import user_email
from allauth.core import context
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin
from allauth.utils import build_absolute_uri
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import Accounts
from utility.template import ToastTag


def _base64_encode(value: str):
    return b64encode(value.encode("utf-8")).decode("utf-8")


class AccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix: str, email: str, context: dict):
        with ThreadPoolExecutor() as executor:
            executor.submit(super().send_mail, template_prefix, email, context)

    def respond_email_verification_sent(self, request: HttpRequest, user) -> HttpResponseRedirect:
        request.session["email"] = request.POST.get("email")
        return super().respond_email_verification_sent(request, user)

    def get_login_redirect_url(self, request: HttpRequest) -> str:
        user: Union["Accounts", "AnonymousUser"] = request.user

        if user.is_authenticated:
            if not user.has_usable_password():
                form = ResetPasswordForm(data={"email": user.email})
                if form.is_valid():
                    form.save(request)
                    messages.info(
                        request,
                        _("We have sent a password setup link to your email. Please set your password."),
                        extra_tags=str(ToastTag()),
                    )

            if not user.is_required_info():
                return resolve_url("accounts:info")

        return super().get_login_redirect_url(request)

    def send_account_already_exists_mail(self, email):
        signup_url = build_absolute_uri(context.request, reverse("account_signup"))
        query_params = {"email": _base64_encode(email)}
        password_reset_url = (
            build_absolute_uri(context.request, reverse("account_reset_password")) + "?" + urlencode(query_params)
        )
        ctx = {
            "request": context.request,
            "signup_url": signup_url,
            "password_reset_url": password_reset_url,
        }
        self.send_mail("account/email/account_already_exists", email, ctx)

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, False)
        validated_data = form.cleaned_data
        user.name = validated_data["name"]
        user.gender = validated_data["gender"]
        user.phone = validated_data["phone"]
        if commit:
            user.save()
        return user


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        if sociallogin.is_existing:
            return

        email = user_email(sociallogin.user)
        try:
            user = get_user_model().objects.get(email=email)
            sociallogin.connect(request, user)
            email_address, created = EmailAddress.objects.get_or_create(user=user, email=user.email)
            if not email_address.verified:
                email_address.verified = True
                email_address.primary = True
                email_address.save()
        except get_user_model().DoesNotExist:
            return

    def populate_user(self, request: HttpRequest, sociallogin: SocialLogin, data: dict):
        user = super().populate_user(request, sociallogin, data)
        user.name = f"{data.get('last_name')} {data.get('first_name')}"
        return user

    def send_notification_mail(self, *args, **kwargs):
        return super().send_notification_mail(*args, **kwargs)
