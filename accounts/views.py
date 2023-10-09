from allauth.account.views import LoginView as AllauthLoginView
from allauth.account.views import LogoutView as AllauthLogoutView
from allauth.account.views import PasswordResetView as AllauthPasswordResetView
from allauth.account.views import SignupView as AllauthSignupView

from utility.form.mixin import LayoutBlankMixin, LayoutMixin
from utility.template.layout import TemplateLayout


class SignupView(LayoutBlankMixin, AllauthSignupView):
    template_name = "signup.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class LoginView(LayoutBlankMixin, AllauthLoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response


class LogoutView(LayoutMixin, AllauthLogoutView):
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class PasswordResetView(AllauthPasswordResetView):
    template_name = "password_reset.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        return TemplateLayout(self.request, context)
