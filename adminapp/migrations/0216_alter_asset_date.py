# Generated by Django 4.1.2 on 2023-12-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0215_asset_date_depreciation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
