# Generated by Django 4.2.5 on 2023-09-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0013_med_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=255)),
                ('supplier_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('drug_license_number', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
