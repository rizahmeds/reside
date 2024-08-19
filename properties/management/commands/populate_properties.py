import random

from django.db import transaction
from django.core.management.base import BaseCommand

from properties.factories import PropertyFactory, RoomsFactory
from properties.models import Property, Rooms
from users.models import LandLoard


class Command(BaseCommand):
    help = "Generates test data for properties app..."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Property, Rooms]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Add dummy properties
        for land_loard in LandLoard.objects.all():
            property_type = random.choice([x[0] for x in Property.PropertyType.choices])
            property = PropertyFactory(property_type=property_type, land_loard=land_loard)

        # Add dummy rooms
        for property in Property.objects.filter(property_type=Property.PropertyType.ROOMS):
            room = RoomsFactory(property=property)
            room.room_no = property.id
            room.save()
