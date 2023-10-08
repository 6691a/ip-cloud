from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from utility.model import TimeStampedModel

from .choices import Gender
from .managers import AccountsManager


class Accounts(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(_("email address"), unique=True, db_column="email")
    first_name = models.CharField(
        _("first name"), max_length=150, blank=True, db_column="first_name"
    )
    last_name = models.CharField(_("last name"), max_length=150, blank=True, db_column="last_name")
    gender = models.CharField(
        _("gender"), max_length=1, choices=Gender.choices, blank=True, db_column="gender"
    )
    phone = PhoneNumberField(_("phone"), blank=True, db_column="phone")
    is_active = models.BooleanField(
        _("active"),
        default=True,
        db_column="active",
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        _("staff"),
        default=False,
        db_column="staff",
        help_text=_("Designates whether the user can log into this admin site."),
    )

    objects = AccountsManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Accounts")
        verbose_name_plural = _("Accounts")
