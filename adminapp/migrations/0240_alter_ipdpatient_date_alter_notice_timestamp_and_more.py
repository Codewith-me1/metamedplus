# Generated by Django 4.1.2 on 2024-01-24 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0239_patient_cause_of_emergebcy_patient_emergency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipdpatient',
            name='date',
            field=models.DateField(default=datetime.date(2024, 1, 25)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='opdpatient',
            name='date',
            field=models.DateField(default=datetime.date(2024, 1, 25)),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='date',
            field=models.DateField(default=datetime.date(2024, 1, 25)),
        ),
    ]