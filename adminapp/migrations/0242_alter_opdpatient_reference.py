# Generated by Django 4.1.2 on 2024-01-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0241_alter_appointmentdetails_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opdpatient',
            name='reference',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
    ]