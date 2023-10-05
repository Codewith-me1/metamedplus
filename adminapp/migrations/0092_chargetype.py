# Generated by Django 4.2.5 on 2023-09-30 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0091_blooddonation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('charge_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.module_charge')),
            ],
        ),
    ]