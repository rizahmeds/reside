from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import AccountsManager


class AccountsModel(AbstractUser):
    username = None
    email = models.EmailField(
        "Email Address",
        unique=True,
    )
    phone_number = PhoneNumberField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = AccountsManager()

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")


