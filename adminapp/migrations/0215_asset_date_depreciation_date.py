# Generated by Django 4.1.2 on 2023-12-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0214_bankbook_type_alter_payroll_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='depreciation',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
