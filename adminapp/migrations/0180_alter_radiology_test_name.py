# Generated by Django 4.1.2 on 2023-11-21 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0179_alter_payroll_date_alter_radiology_test_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiology',
            name='test_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
