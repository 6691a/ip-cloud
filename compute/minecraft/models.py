from django.db import models

from compute.models import Game


class Minecraft(Game):
    class Meta(Game.Meta):
        verbose_name = "Minecraft"
        verbose_name_plural = "Minecraft"
