# Generated by Django 4.2.5 on 2023-09-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0092_chargetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax_cat',
            name='percentage',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]