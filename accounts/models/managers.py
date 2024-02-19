from typing import TYPE_CHECKING, Any, Optional

from django.contrib.auth.base_user import BaseUserManager

if TYPE_CHECKING:
    from .models import Accounts


class AccountsManager(BaseUserManager["Accounts"]):
    def create_user(self, email: str, password: Optional[str], **kwargs: Any) -> "Accounts":
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: Optional[str], **kwargs: Any) -> "Accounts":
        """
        Creates and saves a superuser with the given email and password.
        """
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        return self.create_user(email, password, **kwargs)
