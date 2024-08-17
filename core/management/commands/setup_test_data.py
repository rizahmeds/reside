import random

from django.db import transaction
from django.core.management.base import BaseCommand

from core.factories import (
    CustomUserFactory,
    LandLoardFactory,
    PropertyFactory,
    RoomsFactory,
    TenantFactory,
)
from properties.models import Property
from users.models import CustomUser, LandLoard, Tenant

NUM_USERS = 50


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [CustomUser, LandLoard, Tenant, Property]
        for m in models:
            m.objects.exclude(id=456).delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        users = []
        for _ in range(NUM_USERS):
            role = random.choice([x[0] for x in CustomUser.Types.choices])
            user = CustomUserFactory(role=role)
            users.append(user)

        # Add some land_loard
        land_loards = []
        for user in users[:25]:
            land_loard = LandLoardFactory(user=user)
            land_loards.append(land_loard)

        # Add some Tenant
        for user in users[25:]:
            TenantFactory(user=user)

        # Add some properties
        properties = []
        for land_loard in land_loards:
            property_type = random.choice([x[0] for x in Property.PropertyType.choices])
            property = PropertyFactory(property_type=property_type, land_loard=land_loard)
            properties.append(property)

        # Add some rooms
        for index, property in enumerate(properties, start=1):
            # property_type = random.choice([x[0] for x in Property.PropertyType.choices])
            room = RoomsFactory(property=property)
            room.room_no = index
            room.save()