# Generated by Django 4.2.5 on 2023-10-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0108_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_acc',
            name='unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
