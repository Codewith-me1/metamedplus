# Generated by Django 4.2.5 on 2023-09-28 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0074_alter_ipdpatients_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IpdPatients',
            new_name='IpdPatient',
        ),
    ]
