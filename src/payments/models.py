from django.db import models
from django.utils.translation import gettext_lazy as _

from properties.models import Rooms


class MonthlyBill(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    month = models.DateField(
        help_text="The first day of the month for which the bill is generated"
    )
    electricity_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    water_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    garbage_collection_bill = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    class Meta:
        verbose_name = _("Monthly Bill")
        verbose_name_plural = _("Monthly Bills")
        unique_together = ("room", "month")

    def save(self, *args, **kwargs):
        self.total_amount = (
            self.electricity_bill + self.water_bill + self.garbage_collection_bill
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill for {self.room} for {self.month.strftime('%B %Y')}"


class Payment(models.Model):
    monthly_bill = models.OneToOneField(
        MonthlyBill, on_delete=models.CASCADE, related_name="payment"
    )
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return f"Payment for {self.monthly_bill}"

    def save(self, *args, **kwargs):
        if self.amount_paid >= self.monthly_bill.total_amount:
            self.is_paid = True
        else:
            self.is_paid = False
        super().save(*args, **kwargs)
