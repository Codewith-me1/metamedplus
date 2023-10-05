# Generated by Django 4.2.5 on 2023-09-28 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0078_alter_opdpatient_any_known_alter_opdpatient_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_med',
            name='amount',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchase_med',
            name='batch_amount',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='purchase_med',
            name='mrp',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='purchase_med',
            name='purchase_price',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='purchase_med',
            name='sale_price',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchase_med',
            name='tax_percentage',
            field=models.IntegerField(max_length=20),
        ),
    ]
