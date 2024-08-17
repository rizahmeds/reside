from django.contrib import admin

from properties.models import Property, Rooms


@admin.register(Property)
class AdminProperty(admin.ModelAdmin):
    list_display = ("land_loard", "property_type")

@admin.register(Rooms)
class AdminRooms(admin.ModelAdmin):
    list_display = ("room_no", 'tenant', 'capacity')
