# Generated by Django 4.1.2 on 2023-11-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0184_complaintype_alter_payroll_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain_source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]