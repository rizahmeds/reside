# Generated by Django 5.1 on 2024-08-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[("LAND_LOARD", "LandLoard"), ("TENANT", "Tenant")],
                default="LAND_LOARD",
                max_length=20,
            ),
        ),
    ]
