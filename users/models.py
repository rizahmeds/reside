from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .manager import LandLoardManager, TenantManager, CustomUserManager


class CustomUser(AbstractUser):
    class Types(models.TextChoices):
        LAND_LOARD = ("LAND_LOARD", "LandLoard")
        TENANT = ("TENANT", "Tenant")

    username = None
    email = models.EmailField(
        "Email Address",
        unique=True,
    )
    role = models.CharField(
        max_length=20, choices=Types.choices, default=Types.LAND_LOARD
    )
    phone_number = PhoneNumberField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class LandLoard(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = LandLoardManager()

    class Meta:
        verbose_name = _("Land Lord")
        verbose_name_plural = _("Land Lords")

    def __str__(self) -> str:
        return str(self.user.email)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Tenant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = TenantManager()

    class Meta:
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")

    def __str__(self) -> str:
        return str(self.user.email)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
