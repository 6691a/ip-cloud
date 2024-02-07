from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect


class AccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix: str, email: str, context: dict):
        # TODO: Kafka를 통한 비동기 처리로 변경 예정
        super().send_mail(template_prefix, email, context)

    def respond_email_verification_sent(self, request: HttpRequest, user) -> HttpResponseRedirect:
        request.session["email"] = request.POST.get("email")
        return super().respond_email_verification_sent(request, user)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request: HttpRequest, sociallogin: SocialLogin):
        user = sociallogin.user
        if not user.has_usable_password():
            return redirect("accounts:reset_password", title="Reset Password")
