# Generated by Django 4.2.5 on 2023-09-21 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0023_alter_donor_det_discount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_name', models.CharField(max_length=255)),
                ('issue_date', models.CharField(max_length=20)),
                ('hospital_doctor', models.CharField(blank=True, max_length=255, null=True)),
                ('technician', models.CharField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('bag', models.CharField(blank=True, max_length=20, null=True)),
                ('charge_category', models.CharField(blank=True, max_length=20, null=True)),
                ('charge_name', models.CharField(blank=True, max_length=255, null=True)),
                ('standard_charge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Blood Donations',
            },
        ),
    ]
