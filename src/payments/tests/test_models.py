from django.test import TestCase
from datetime import date

from payments.models import Payment, ExpenseCategory, Expense, PaymentDetail
from properties.factories import RoomsFactory


class TestPayment(TestCase):
    @classmethod
    def setUpTestData(cls):
        # cls.room = Rooms.objects.create(name="Room 1")
        cls.room = RoomsFactory()
        cls.payment = Payment.objects.create(
            room=cls.room,
            amount=1000,
            for_month=date.today().replace(day=1),
            is_paid=True,
        )

    def test_payment_str(self):
        self.assertEqual(str(self.payment), f"Payment for room number {self.room}")

    def test_is_late(self):
        self.payment.payment_date = self.payment.for_month.replace(day=11)
        self.assertTrue(self.payment.is_late)
        self.payment.payment_date = self.payment.for_month.replace(day=9)
        self.assertFalse(self.payment.is_late)


class TestExpenseCategory(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = ExpenseCategory.objects.create(name="Utilities")

    def test_expense_category_str(self):
        self.assertEqual(str(self.category), "Utilities")


class TestExpense(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.room = RoomsFactory()
        cls.category = ExpenseCategory.objects.create(name="Utilities")
        cls.expense = Expense.objects.create(
            room=cls.room,
            category=cls.category,
            amount=200.50,
            date=date.today(),
            description="Electricity bill",
        )

    def test_expense_fields(self):
        self.assertEqual(self.expense.room, self.room)
        self.assertEqual(self.expense.category, self.category)
        self.assertEqual(self.expense.amount, 200.50)
        self.assertEqual(self.expense.date, date.today())
        self.assertEqual(self.expense.description, "Electricity bill")


class TestPaymentDetail(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.room = RoomsFactory()
        cls.payment = Payment.objects.create(
            room=cls.room,
            amount=1000,
            for_month=date.today().replace(day=1),
            is_paid=True,
        )
        cls.category = ExpenseCategory.objects.create(name="Utilities")
        cls.payment_detail = PaymentDetail.objects.create(
            payment=cls.payment, category=cls.category, amount=100
        )

    def test_payment_detail_str(self):
        self.assertEqual(
            str(self.payment_detail),
            f"{self.category}: {self.payment_detail.amount} for {self.payment}",
        )

    def test_payment_detail_fields(self):
        self.assertEqual(self.payment_detail.payment, self.payment)
        self.assertEqual(self.payment_detail.category, self.category)
        self.assertEqual(self.payment_detail.amount, 100)
