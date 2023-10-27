# Generated by Django 4.2.5 on 2023-10-09 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0112_remove_sales_invoice_without_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales_invoice',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='sales_invoice',
            name='discount_amount',
        ),
        migrations.RemoveField(
            model_name='sales_invoice',
            name='item',
        ),
        migrations.RemoveField(
            model_name='sales_invoice',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sales_invoice',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='sales_invoice',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='sales_invoice',
            name='tax_amount',
        ),
        migrations.RemoveField(
            model_name='sales_invoice',
            name='total',
        ),
        migrations.RemoveField(
            model_name='sales_invoice',
            name='unit',
        ),
        migrations.CreateModel(
            name='Item_Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('qty', models.DecimalField(decimal_places=3, max_digits=13)),
                ('unit', models.CharField(max_length=13)),
                ('price', models.DecimalField(decimal_places=3, max_digits=13)),
                ('discount', models.DecimalField(decimal_places=3, max_digits=13)),
                ('discount_amount', models.DecimalField(decimal_places=3, max_digits=13)),
                ('tax', models.DecimalField(decimal_places=3, max_digits=5)),
                ('tax_amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('total', models.DecimalField(decimal_places=3, max_digits=13)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.sales_invoice')),
            ],
        ),
    ]