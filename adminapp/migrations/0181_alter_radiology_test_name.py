# Generated by Django 4.1.2 on 2023-11-21 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0180_alter_radiology_test_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiology',
            name='test_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.radiology_test'),
        ),
    ]
