# Generated by Django 4.2.5 on 2023-09-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0046_alter_referralperson_commission_ambulance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_type', models.CharField(max_length=255)),
                ('bill_no', models.CharField(max_length=255)),
                ('bill_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payee', models.CharField(max_length=255)),
                ('commission_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('commission_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
