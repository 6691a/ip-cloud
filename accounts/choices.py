from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Gender(TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
