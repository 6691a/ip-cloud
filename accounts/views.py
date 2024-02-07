from allauth.account.utils import send_email_confirmation
from allauth.account.views import ConfirmEmailView as AllauthConfirmEmailView
from allauth.account.views import (
    EmailVerificationSentView as AllauthEmailVerificationSentView,
)
from allauth.account.views import LoginView as AllauthLoginView
from allauth.account.views import LogoutView as AllauthLogoutView
from allauth.account.views import PasswordResetView as AllauthPasswordResetView
from allauth.account.views import SignupView as AllauthSignupView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import translation
from django.views.generic import FormView
from phonenumber_field.widgets import localized_choices

from accounts.forms import ReVerificationForm, SignupForm
from utility.form.mixin import LayoutBlankMixin, LayoutMixin

User = get_user_model()


class SignupView(LayoutBlankMixin, AllauthSignupView):
    template_name = "signup.html"
    form_class = SignupForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(
            countries=localized_choices(translation.get_language()), **kwargs
        )
        return context


class LoginView(LayoutBlankMixin, AllauthLoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


class LogoutView(LayoutMixin, AllauthLogoutView):
    pass


class VerificationView(LayoutBlankMixin, AllauthEmailVerificationSentView, FormView):
    template_name = "verification.html"
    form_class = ReVerificationForm
    success_url = "/accounts/confirm-email/"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["email"] = self.request.session.get("email")
        return context

    def post(self, request, *args, **kwargs):
        """
        Resend email confirmation.
        """
        form = self.get_form()
        if form.is_valid():
            if email := form.cleaned_data.get("email"):
                user = User.objects.get(email=email)
                send_email_confirmation(request, user, email)
                messages.info(
                    request,
                    "Please try again in a few moments if you did not receive the resend email.",
                    extra_tags="resend",
                )
            else:
                messages.error(request, "Error sending confirmation email.", extra_tags="resend")

        return self.form_valid(form)


class ConfirmView(LayoutBlankMixin, AllauthConfirmEmailView):
    pass


class PasswordResetView(LayoutBlankMixin, AllauthPasswordResetView):
    template_name = "rest_password.html"
    redirect_authenticated_user = True


class PasswordForgotView(LayoutBlankMixin, AllauthPasswordResetView):
    template_name = "forgot_password.html"
    redirect_authenticated_user = True
    success_url = "/accounts/password/forgot/done/"
