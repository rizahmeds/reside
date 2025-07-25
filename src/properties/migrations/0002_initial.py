# Generated by Django 5.1 on 2025-07-19 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='land_loard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.landloard'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='tenant',
            field=models.ManyToManyField(blank=True, to='users.tenant'),
        ),
        migrations.AddField(
            model_name='electricityreading',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electricity_readings', to='properties.rooms'),
        ),
        migrations.AlterUniqueTogether(
            name='electricityreading',
            unique_together={('room', 'reading_date')},
        ),
    ]
