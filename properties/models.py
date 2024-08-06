from django.db import models
from django.utils.translation import gettext_lazy as _

class Property(models.Model):
    class PropertyType(models.TextChoices):
        ROOMS = _("Rooms")
        FLATS = _("FLATS")
    
    property_type = models.CharField(
        max_length=2,
        choices=PropertyType.choices,
        default=PropertyType.ROOMS,
    )

    address = models.CharField(max_length=100)

        
