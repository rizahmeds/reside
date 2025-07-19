from django.contrib import admin

from payments.models import MonthlyBill, Payment


@admin.register(MonthlyBill)
class AdminMonthlyBill(admin.ModelAdmin):
    list_display = (
        "room",
        "month",
        "electricity_bill",
        "water_bill",
        "garbage_collection_bill",
        "total_amount",
    )


@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    list_display = ("monthly_bill", "amount_paid", "payment_date", "is_paid")
