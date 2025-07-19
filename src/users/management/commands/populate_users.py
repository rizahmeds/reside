import random

from django.db import transaction
from django.core.management.base import BaseCommand

from users.factories import (
    CustomUserFactory,
    LandLoardFactory,
    TenantFactory,
)
from users.models import CustomUser, LandLoard, Tenant

NUM_USERS = 50


class Command(BaseCommand):
    help = "Generates test data for users..."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [CustomUser, LandLoard, Tenant]
        for m in models:
            m.objects.exclude(id=456).delete()

        self.stdout.write("Creating new data...")
        # Create dummy users
        for _ in range(NUM_USERS):
            role = random.choice([x[0] for x in CustomUser.Types.choices])
            user = CustomUserFactory(role=role)

        # Add dummy land_loard
        for user in CustomUser.objects.all()[:25]:
            land_loard = LandLoardFactory(user=user)

        # Add dummy Tenant
        for user in CustomUser.objects.all()[:25]:
            TenantFactory(user=user)
