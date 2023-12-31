# Generated by Django 4.1.2 on 2023-11-25 09:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0188_operation_category_operation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='date',
            field=models.DateField(default=datetime.date(2023, 11, 25)),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=20)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.medicine')),
            ],
        ),
    ]
