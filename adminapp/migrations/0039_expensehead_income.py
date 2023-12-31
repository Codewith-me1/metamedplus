# Generated by Django 4.2.5 on 2023-09-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0038_incomehead'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_head', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demo', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('invoice_number', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('document', models.FileField(blank=True, null=True, upload_to='income_documents/')),
                ('description', models.TextField()),
            ],
        ),
    ]
