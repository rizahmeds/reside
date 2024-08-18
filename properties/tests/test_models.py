from django.test import TestCase

from users.models import LandLoard, Tenant
from properties.models import Property, Rooms

class TestRooms(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.land_loard = LandLoard.objects.create(name="John Doe")
        cls.property = Property.objects.create(
            land_loard=cls.land_loard,
            property_type=Property.PropertyType.ROOMS,
            address="123 Main St",
            city="Anytown",
            state="Anystate",
            country="Anycountry",
            zip_code="12345"
        )
        cls.tenant = Tenant.objects.create(name="Jane Smith")
        cls.room = Rooms.objects.create(
            property=cls.property,
            room_no="101",
            tenant=cls.tenant,
            capacity=2,
            base_rent=500
        )

    def test_room_str(self):
        self.assertEqual(str(self.room), "101")

    def test_room_fields(self):
        self.assertEqual(self.room.property, self.property)
        self.assertEqual(self.room.room_no, "101")
        self.assertEqual(self.room.tenant, self.tenant)
        self.assertEqual(self.room.capacity, 2)
        self.assertEqual(self.room.base_rent, 500)