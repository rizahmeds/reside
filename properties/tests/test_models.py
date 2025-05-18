from django.test import TestCase

from users.models import CustomUser, LandLoard, Tenant
from properties.models import Property, Rooms


class TestRooms(TestCase):
    @classmethod
    def setUpTestData(cls):
        land_loard = CustomUser.objects.create_user(
            email="landloard@example.com",
            password="password123",
            role=CustomUser.Types.LAND_LOARD,
            phone_number="+1234567890",
        )
        cls.land_loard = LandLoard.objects.create(user=land_loard)
        cls.property = Property.objects.create(
            land_loard=cls.land_loard,
            property_type=Property.PropertyType.ROOMS,
            address="123 Main St",
            city="Anytown",
            state="Anystate",
            country="Anycountry",
            zip_code="12345",
        )
        tenant = CustomUser.objects.create_user(
            email="tenant@example.com",
            password="password123",
            role=CustomUser.Types.TENANT,
            phone_number="+0987654321",
        )
        cls.tenant = Tenant.objects.create(user=tenant)
        cls.room = Rooms.objects.create(
            property=cls.property,
            room_no="101",
            tenant=cls.tenant,
            capacity=2,
            base_rent=500,
        )

    def test_room_str(self):
        self.assertEqual(str(self.room), "101")

    def test_room_fields(self):
        self.assertEqual(self.room.property, self.property)
        self.assertEqual(self.room.room_no, "101")
        self.assertEqual(self.room.tenant, self.tenant)
        self.assertEqual(self.room.capacity, 2)
        self.assertEqual(self.room.base_rent, 500)
