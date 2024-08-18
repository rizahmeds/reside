from django.db import models
from django.utils.translation import gettext_lazy as _

from properties.models import Rooms

class Payment(models.Model):

    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return f'Payment for room number {self.room}'



class ElectricityBill(models.Model):

    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    consumption = models.IntegerField()
    rate = models.IntegerField(default=10)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("Electricity Bill")
        verbose_name_plural = _("Electricity Bills")

    def __str__(self):
        return f'Bill for room number {self.room}'
