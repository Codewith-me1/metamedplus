# Generated by Django 4.1.2 on 2024-01-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0237_alter_visitors_out_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='out_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
