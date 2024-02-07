from random import randint

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import IntegrityError, models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords
from structlog import get_logger

from utility.model import TimeStampedModel

from .choices import Gender
from .managers import AccountsManager

logging = get_logger(__name__)


class Accounts(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(_("email address"), unique=True, db_column="email")
    name = models.CharField(_("name"), max_length=30, blank=True, db_column="name")
    gender = models.CharField(
        _("gender"), max_length=1, choices=Gender.choices, blank=True, db_column="gender"
    )
    # 12자리의 랜덤 숫자를 만든다
    alias = models.CharField(
        _("alias"),
        max_length=12,
        unique=True,
        blank=True,
        null=True,
        db_column="alias",
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
    history = HistoricalRecords()
    objects = AccountsManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def _make_random_alias(self, digits: int = 12) -> str:
        """
        alias를 생성한다.
        """
        return "".join([str(randint(0, 9)) for _ in range(randint(1, digits))]).zfill(digits)

    def save(self, *args, **kwargs):
        if self.is_staff or self.is_superuser:
            super().save(*args, **kwargs)
            return

        err: Exception | None = None

        for i in range(5):
            try:
                self.alias = self._make_random_alias(12)
                super().save(*args, **kwargs)
                break
            except IntegrityError:
                continue
        else:
            logging.error(f"Infinite loop occurred while creating alias for {self.email}")
            if err:
                raise err
