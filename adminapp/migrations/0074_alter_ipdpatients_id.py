# Generated by Django 4.2.5 on 2023-09-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0073_alter_ipdpatients_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipdpatients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
