from django.db import models
from django.utils.translation import gettext_lazy as _

from properties.manager import PropertyManager, RoomsManager
from users.models import LandLoard, Tenant


class Property(models.Model):
    class PropertyType(models.TextChoices):
        ROOMS = "ROOMS", "Rooms"
        FLATS = "FLATS", "Flats"

    land_loard = models.ForeignKey(LandLoard, on_delete=models.CASCADE, null=True)

    property_type = models.CharField(
        max_length=20, choices=PropertyType.choices, default=PropertyType.ROOMS
    )

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)

    objects = PropertyManager()

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def __str__(self):
        return str(self.land_loard)


class Rooms(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=20)
    tenant = models.ManyToManyField(Tenant, blank=True)
    capacity = models.IntegerField(default=3)
    base_rent = models.IntegerField()

    objects = RoomsManager()

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")

    def __str__(self):
        return str(self.room_no)


class ElectricityReading(models.Model):
    room = models.ForeignKey(
        Rooms, on_delete=models.CASCADE, related_name="electricity_readings"
    )
    reading = models.PositiveIntegerField()
    reading_date = models.DateField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)

    class Meta:
        verbose_name = _("Electricity Reading")
        verbose_name_plural = _("Electricity Readings")
        unique_together = ("room", "reading_date")
        ordering = ["-reading_date"]

    def __str__(self):
        return f"Reading for Room {self.room.room_no} on {self.reading_date}"

    def get_previous_reading(self):
        return (
            ElectricityReading.objects.filter(
                room=self.room, reading_date__lt=self.reading_date
            )
            .order_by("-reading_date")
            .first()
        )

    @property
    def consumed_units(self):
        previous_reading = self.get_previous_reading()
        if previous_reading:
            return self.reading - previous_reading.reading
        return self.reading

    @property
    def bill_amount(self):
        return self.consumed_units * self.unit_price