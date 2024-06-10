from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import DeleteTimeStampModelManager


class TimeStampModel(models.Model):
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


class DeleteTimeStampModel(TimeStampModel):
    deleted = models.DateTimeField(
        null=True, blank=True, help_text="Date and time on which the network address was deleted."
    )

    objects = DeleteTimeStampModelManager()

    def delete(self, using=None, keep_parents=False):
        """
        Soft delete the object by setting the ``deleted`` field to the current date and time.
        """
        self.deleted = timezone.now()
        self.save()

    class Meta:
        abstract = True
