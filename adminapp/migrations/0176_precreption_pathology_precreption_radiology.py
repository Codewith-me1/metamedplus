# Generated by Django 4.1.2 on 2023-11-17 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0175_alter_donor_det_options_alter_donor_det_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='precreption',
            name='pathology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.pathology'),
        ),
        migrations.AddField(
            model_name='precreption',
            name='radiology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.radiology'),
        ),
    ]
