from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.forms import ResetPasswordForm
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import resolve_url
from django.utils.translation import gettext as _

from utility.template import ToastTag


class AccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix: str, email: str, context: dict):
        # TODO: Kafka를 통한 비동기 처리로 변경 예정
        super().send_mail(template_prefix, email, context)

    def respond_email_verification_sent(self, request: HttpRequest, user) -> HttpResponseRedirect:
        request.session["email"] = request.POST.get("email")
        return super().respond_email_verification_sent(request, user)

    def get_login_redirect_url(self, request: HttpRequest) -> str:
        user = request.user
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
                return resolve_url("accounts:reset_password")

        return super().get_login_redirect_url(request)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request: HttpRequest, sociallogin: SocialLogin, data: dict):
        user = super().populate_user(request, sociallogin, data)
        user.name = f"{data.get('last_name')} {data.get('first_name')}"
        return user
