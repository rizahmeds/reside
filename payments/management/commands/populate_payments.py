import random
from django.db import transaction
from django.core.management.base import BaseCommand

from payments.factories import ExpenseFactory, PaymentDetailFactory, PaymentFactory, ExpenseCategoryFactory
from payments.models import Payment, ExpenseCategory, Expense, PaymentDetail
from properties.models import Rooms

class Command(BaseCommand):
    help = "Generates test data for payments app..."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Payment, ExpenseCategory, Expense, PaymentDetail]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        
        expense_categories = []
        for expense in ['Electricity', 'Water', 'Garbage']:
            category = ExpenseCategoryFactory(name=expense)
            expense_categories.append(category)

        # Add payments for each rooms
        payments = []
        for room in Rooms.objects.all():
            payment = PaymentFactory(room=room)
            payments.append(payment)
            ExpenseFactory(room=room, category=random.choice(expense_categories))
        
        # for payment in payments:
        #     payment_detail = PaymentDetailFactory(payment=payment)