# Generated by Django 4.1.2 on 2023-11-23 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0186_complain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='consultant_doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.addstaff'),
        ),
    ]
