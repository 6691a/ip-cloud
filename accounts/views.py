from allauth.account.views import LoginView as AllauthLoginView
from allauth.account.views import LogoutView as AllauthLogoutView
from allauth.account.views import PasswordResetView as AllauthPasswordResetView
from allauth.account.views import SignupView as AllauthSignupView

from utility.template.layout import TemplateLayout, TemplateLayoutBlank


class SignupView(AllauthSignupView):
    template_name = "signup.html"


class LoginView(AllauthLoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        return TemplateLayoutBlank(self.request, context)


class LogoutView(AllauthLogoutView):
    template_name = "logout.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        return TemplateLayout(self.request, context)


class PasswordResetView(AllauthPasswordResetView):
    template_name = "password_reset.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        return TemplateLayout(self.request, context)
