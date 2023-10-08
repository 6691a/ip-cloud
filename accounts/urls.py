from django.urls import path

from .views import LoginView, LogoutView, PasswordResetView, SignupView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password/reset/", PasswordResetView.as_view(), name="password_reset"),
]
