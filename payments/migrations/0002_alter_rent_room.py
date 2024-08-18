# Generated by Django 5.1 on 2024-08-17 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('properties', '0006_rooms_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='room',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='properties.rooms'),
        ),
    ]