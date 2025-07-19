from django.contrib import admin

from payments.admin import AdminRentInline
from properties.models import ElectricityReading, Property, Rooms


@admin.register(Property)
class AdminProperty(admin.ModelAdmin):
    list_display = ("land_loard", "property_type")


@admin.register(Rooms)
class AdminRooms(admin.ModelAdmin):
    list_display = ("room_no", "tenant", "capacity")
    inlines = [AdminRentInline]


@admin.register(ElectricityReading)
class AdminElectricityReading(admin.ModelAdmin):
    list_display = (
        "room",
        "reading_date",
        "reading",
        "unit_price",
        "consumed_units",
        "bill_amount",
    )
    list_filter = ("room", "reading_date")
    search_fields = ("room__room_no",)