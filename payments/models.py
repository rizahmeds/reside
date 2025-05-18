from django.db import models
from django.utils.translation import gettext_lazy as _

from properties.models import Rooms


class Payment(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    for_month = models.DateField(
        help_text="The first day of the month for which the payment is made"
    )
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        # return f"Payment of {self.amount} for {self.room} by {self.tenant} for {self.for_month.strftime('%B %Y')}"
        return f"Payment for room number {self.room}"

    @property
    def is_late(self):
        return self.payment_date > self.for_month.replace(day=10)


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Expense Category")
        verbose_name_plural = _("Expense Categories")

    def __str__(self):
        return self.name


class Expense(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)


class PaymentDetail(models.Model):
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="details"
    )
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category}: {self.amount} for {self.payment}"
