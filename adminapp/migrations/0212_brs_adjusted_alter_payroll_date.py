# Generated by Django 4.1.2 on 2023-12-02 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0211_depreciation'),
    ]

    operations = [
        migrations.AddField(
            model_name='brs',
            name='adjusted',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='date',
            field=models.DateField(default=datetime.date(2023, 12, 3)),
        ),
    ]
