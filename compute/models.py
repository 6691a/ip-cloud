from uuid import uuid4

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from taggit.managers import TaggableManager

from utility.model import TimeStampModel


class Compute(TimeStampModel):
    name = models.CharField(max_length=100, help_text="name of the instance.")
    uuid = models.UUIDField(default=uuid4, editable=False, help_text="instance unique identifier.")
    region = models.ForeignKey("region.Region", on_delete=models.CASCADE, related_name="compute")
    address = models.ForeignKey("network.Address", on_delete=models.CASCADE, related_name="compute")
    tags = TaggableManager()

    class Meta:
        verbose_name = "Compute"
        verbose_name_plural = "Computes"
        abstract = True
        indexes = [
            models.Index(fields=["uuid"], name="instance_uuid_idx"),
            models.Index(fields=["region"], name="instance_region_idx"),
        ]


class Game(Compute):
    class Meta(Compute.Meta):
        verbose_name = "Game"
        verbose_name_plural = "Games"
        abstract = True


class GameWhiteList(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    game = GenericForeignKey("content_type", "object_id")
    white_list = models.ForeignKey("network.WhiteList", on_delete=models.CASCADE, related_name="game_whitelists")
