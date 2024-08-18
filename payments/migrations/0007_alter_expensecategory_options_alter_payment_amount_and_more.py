# Generated by Django 5.1 on 2024-08-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_expensecategory_rename_created_payment_payment_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expensecategory',
            options={'verbose_name': 'Expense Category', 'verbose_name_plural': 'Expense Categories'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]