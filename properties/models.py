from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import LandLoard, Tenant


class Property(models.Model):
    class PropertyType(models.TextChoices):
        ROOMS = "ROOMS", "Rooms"
        FLATS = "FLATS", "Flats"

    land_loard = models.OneToOneField(LandLoard, on_delete=models.CASCADE, null=True)

    property_type = models.CharField(
        max_length=20, choices=PropertyType.choices, default=PropertyType.ROOMS
    )

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def __str__(self):
        return str(self.land_loard)


class Rooms(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=20)
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    capacity = models.IntegerField(default=3)
    base_rent = models.IntegerField()

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")

    def __str__(self):
        return str(self.room_no)
