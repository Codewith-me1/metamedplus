# Generated by Django 4.2.5 on 2023-10-15 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0144_bankaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20, unique=True)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=13)),
                ('as_of_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.DecimalField(decimal_places=3, max_digits=13),
        ),
    ]