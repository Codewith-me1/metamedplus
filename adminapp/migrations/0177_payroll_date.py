# Generated by Django 4.1.2 on 2023-11-17 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0176_precreption_pathology_precreption_radiology'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='date',
            field=models.DateField(default=datetime.date(2023, 11, 18)),
        ),
    ]