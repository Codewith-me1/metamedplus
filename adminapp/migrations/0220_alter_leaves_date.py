# Generated by Django 4.1.2 on 2023-12-04 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0219_alter_payroll_date_leaves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaves',
            name='date',
            field=models.DateField(),
        ),
    ]
