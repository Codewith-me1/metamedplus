# Generated by Django 4.1.2 on 2024-01-24 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0240_alter_ipdpatient_date_alter_notice_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentdetails',
            name='priority',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='appointmentdetails',
            name='source',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
    ]
