# Generated by Django 5.1 on 2024-08-17 05:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="property",
            old_name="land_lord",
            new_name="land_loard",
        ),
    ]
