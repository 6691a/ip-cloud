from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("Date time on which the object was created."),
        db_column="created",
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("modified"),
        help_text=_("Date time on which the object was last modified."),
        db_column="modified",
    )

    class Meta:
        abstract = True
