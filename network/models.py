from django.contrib.contenttypes.models import ContentType
from django.db import models
from taggit.managers import TaggableManager

from utility.model import DeleteTimeStampModel, TimeStampModel


class Address(TimeStampModel):
    ip_address_v4 = models.GenericIPAddressField(help_text="IPV4 address for the network.")
    ip_address_v6 = models.GenericIPAddressField(help_text="IPv6 address for the network.", null=True, blank=True)


class WhiteListAddress(models.Model):
    name = models.CharField(max_length=100, help_text="name of the instance.")
    address = models.ForeignKey("network.Address", on_delete=models.CASCADE, related_name="whitelist_address")
    white_list = models.ForeignKey("network.WhiteList", on_delete=models.CASCADE, related_name="whitelist_address")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["address", "white_list"], name="unique_address_white_list")]


class WhiteList(DeleteTimeStampModel):
    name = models.CharField(max_length=100, help_text="name of the instance.")
    address = models.ManyToManyField("network.Address", through="WhiteListAddress", related_name="white_list")
    is_disabled = models.BooleanField(default=False, help_text="Flag to disable the whitelisted IP address.")
    tags = TaggableManager()
