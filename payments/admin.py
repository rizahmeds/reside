from django.contrib import admin

from payments.models import Expense, ExpenseCategory, Payment, PaymentDetail


class AdminRentInline(admin.TabularInline):
    model = Payment
    save_on_top = True
    max_num = 0
    extra = 0
    # fields = ("room",)
    readonly_fields = ("room", "amount", "for_month", "is_paid")


@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    list_display = ("room", "amount", "for_month", "is_paid")


@admin.register(ExpenseCategory)
class AdminExpenseCategory(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Expense)
class AdminExpense(admin.ModelAdmin):
    list_display = ("room", "category", "amount", "date")


@admin.register(PaymentDetail)
class AdminPaymentDetail(admin.ModelAdmin):
    list_display = ("payment", "category", "amount")
