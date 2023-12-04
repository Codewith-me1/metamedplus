# Generated by Django 4.1.2 on 2023-12-03 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0213_alter_brs_adjusted'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankbook',
            name='type',
            field=models.CharField(default='individual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='date',
            field=models.DateField(default=datetime.date(2023, 12, 4)),
        ),
    ]
