# Generated by Django 4.2.5 on 2023-10-15 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0145_bankaccounts_alter_bankaccount_balance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BankAccount',
        ),
    ]
