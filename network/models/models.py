from django.db import models

from utility.model import DeleteTimeStampModel, TimeStampModel


class Address(TimeStampModel):
    cidr = models.CharField(max_length=18, help_text="CIDR format network address.")
    ip_address = models.GenericIPAddressField(help_text="IP address for the network.")
    is_disabled = models.BooleanField(default=False, help_text="Flag to disable the network address.")


class NAT(TimeStampModel):
    protocol = models.CharField(max_length=4, help_text="Protocol for the NAT rule.")
    dst_port = models.PositiveSmallIntegerField(help_text="Destination port for the NAT rule.", null=True, blank=True)


class WhiteList(DeleteTimeStampModel):
    ip_address = models.GenericIPAddressField(help_text="IP address to be whitelisted.")
    instance = models.ForeignKey("instance.Instance", on_delete=models.CASCADE, related_name="whitelist")
    is_disabled = models.BooleanField(default=False, help_text="Flag to disable the whitelisted IP address.")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["ip_address", "instance"], name="unique_ip_address_instance")]
