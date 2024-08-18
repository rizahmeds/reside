from django.contrib import admin

from payments.models import Payment, ElectricityBill


class AdminRentInline(admin.TabularInline):
    model = Payment
    save_on_top = True
    max_num = 0
    extra = 0
    # fields = ("room",)
    readonly_fields = ("room", 'created')



@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    list_display = ("room", 'created')


@admin.register(ElectricityBill)
class AdminElectricityBill(admin.ModelAdmin):
    list_display = ("room", 'consumption', 'rate', 'created')