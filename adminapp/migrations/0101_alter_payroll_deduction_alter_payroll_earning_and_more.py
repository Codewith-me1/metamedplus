# Generated by Django 4.2.5 on 2023-10-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0100_rename_salary_payroll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='deduction',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='earning',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='gross_salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='net_salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='tax',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='tax_percentage',
            field=models.FloatField(default=0.0),
        ),
    ]