from django.contrib import admin

from users.models import LandLoard, Tenant, CustomUser


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ("email", "is_staff", "role")


@admin.register(LandLoard)
class AdminLandLoard(admin.ModelAdmin):
    pass
    # list_display = ('email', 'role', 'date_joined')


@admin.register(Tenant)
class AdminTenant(admin.ModelAdmin):
    pass
    # list_display = ('email', 'role', 'date_joined')
