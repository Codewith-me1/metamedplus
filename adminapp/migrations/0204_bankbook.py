# Generated by Django 4.1.2 on 2023-11-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0203_purchase_composition_alter_payroll_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('particulars', models.CharField(max_length=30, null=True)),
                ('lf', models.IntegerField(max_length=10, null=True)),
                ('debit', models.IntegerField(max_length=20, null=True)),
                ('credit', models.IntegerField(max_length=20, null=True)),
                ('balance', models.IntegerField(max_length=30, null=True)),
            ],
        ),
    ]
