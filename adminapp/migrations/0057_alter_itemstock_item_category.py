# Generated by Django 4.2.5 on 2023-09-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0056_itemstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemstock',
            name='item_category',
            field=models.CharField(max_length=100),
        ),
    ]
