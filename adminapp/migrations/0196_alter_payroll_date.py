# Generated by Django 4.2.6 on 2023-11-30 00:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0195_remove_operation_assistant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='date',
            field=models.DateField(default=datetime.date(2023, 11, 30)),
        ),
    ]
