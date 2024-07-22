from django.db import models
from taggit.managers import TaggableManager

from utility.model import TimeStampModel


class Region(TimeStampModel):
    name = models.CharField(max_length=100, help_text="Region name.")
    description = models.TextField(help_text="Region description.")
    tags = TaggableManager()
