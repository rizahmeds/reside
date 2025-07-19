from django.test import TestCase
from django.utils import timezone
from users.models import CustomUser


class TestCustomUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.landloard_user = CustomUser.objects.create_user(
            email="landloard@example.com",
            password="password123",
            role=CustomUser.Types.LAND_LOARD,
            phone_number="+1234567890",
        )
        cls.tenant_user = CustomUser.objects.create_user(
            email="tenant@example.com",
            password="password123",
            role=CustomUser.Types.TENANT,
            phone_number="+0987654321",
        )

    def test_custom_user_fields(self):
        self.assertEqual(self.landloard_user.email, "landloard@example.com")
        self.assertEqual(self.landloard_user.role, CustomUser.Types.LAND_LOARD)
        self.assertEqual(self.landloard_user.phone_number, "+1234567890")
        self.assertTrue(isinstance(self.landloard_user.created, timezone.datetime))
        self.assertTrue(isinstance(self.landloard_user.updated, timezone.datetime))

        self.assertEqual(self.tenant_user.email, "tenant@example.com")
        self.assertEqual(self.tenant_user.role, CustomUser.Types.TENANT)
        self.assertEqual(self.tenant_user.phone_number, "+0987654321")
        self.assertTrue(isinstance(self.tenant_user.created, timezone.datetime))
        self.assertTrue(isinstance(self.tenant_user.updated, timezone.datetime))

    def test_custom_user_str(self):
        self.assertEqual(str(self.landloard_user), "landloard@example.com")
        self.assertEqual(str(self.tenant_user), "tenant@example.com")

    def test_custom_user_role_choices(self):
        self.assertEqual(self.landloard_user.role, CustomUser.Types.LAND_LOARD)
        self.assertEqual(self.tenant_user.role, CustomUser.Types.TENANT)
        default_user = CustomUser.objects.create_user(
            email="default@example.com", password="password123"
        )
        self.assertEqual(default_user.role, CustomUser.Types.LAND_LOARD)
