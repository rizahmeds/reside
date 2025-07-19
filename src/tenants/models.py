from django.db import models
from django.utils.translation import gettext_lazy as _

from properties.models import Property
from users.models import Tenant


class TenantProfile(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    id_type = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    id_image = models.ImageField(upload_to="tenant_id")

    class Meta:
        verbose_name = _("Tenant Profile")
        verbose_name_plural = _("Tenant Profiles")

    def __str__(self):
        return f"{str(self.tenant.first_name)} {str(self.tenant.last_name)}"
