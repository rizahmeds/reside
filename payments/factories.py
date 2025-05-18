import random
import factory
from factory.django import DjangoModelFactory

from payments.models import Payment, ExpenseCategory, Expense, PaymentDetail
from properties.factories import RoomsFactory


class PaymentFactory(DjangoModelFactory):
    class Meta:
        model = Payment

    room = factory.SubFactory(RoomsFactory)
    amount = factory.Faker("random_number", digits=4)
    payment_date = factory.Faker("date_time")
    for_month = factory.Faker("date")
    is_paid = random.choice([True, False])


class ExpenseCategoryFactory(DjangoModelFactory):
    class Meta:
        model = ExpenseCategory


class ExpenseFactory(DjangoModelFactory):
    class Meta:
        model = Expense

    amount = factory.Faker("random_number", digits=4)
    date = factory.Faker("date")


class PaymentDetailFactory(DjangoModelFactory):
    class Meta:
        model = PaymentDetail

    payment = factory.SubFactory(PaymentFactory)
