# Generated by Django 4.2.5 on 2023-09-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0082_nursingrecord_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('category', models.CharField(max_length=50)),
                ('medicine_name', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=50)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
