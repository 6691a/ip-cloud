from django.urls import path, re_path

from .views import (
    ConfirmView,
    DeleteView,
    LoginView,
    LogoutView,
    PasswordForgotView,
    PasswordResetView,
    ProfileView,
    SignupView,
    VerificationView,
)

app_name = "accounts"


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("confirm-email/", VerificationView.as_view(), name="confirm_email"),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        ConfirmView.as_view(),
        name="account_confirm_email",
    ),
    path("password/reset/", PasswordResetView.as_view(), name="reset_password"),
    path("password/forgot/", PasswordForgotView.as_view(), name="forgot_password"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("delete/", DeleteView.as_view(), name="delete"),
]
