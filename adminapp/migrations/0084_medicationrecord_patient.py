# Generated by Django 4.2.5 on 2023-09-28 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0083_medicationrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationrecord',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.patient'),
        ),
    ]