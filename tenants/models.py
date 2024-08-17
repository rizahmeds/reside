from django.db import models
from django.utils.translation import gettext_lazy as _

from properties.models import Property
from users.models import Tenant


class TenantProfile(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    property = models.OneToOneField(Property, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tenant Profile")
        verbose_name_plural = _("Tenant Profiles")

    def __str__(self):
        return f"{str(self.tenant.first_name)} {str(self.tenant.last_name)}"
