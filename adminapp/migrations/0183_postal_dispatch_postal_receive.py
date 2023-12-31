# Generated by Django 4.1.2 on 2023-11-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0182_visitors_alter_payroll_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postal_dispatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('reference_no', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('note', models.TextField()),
                ('from_title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('attach_document', models.FileField(blank=True, null=True, upload_to='static/postal/receive')),
            ],
        ),
        migrations.CreateModel(
            name='Postal_receive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('reference_no', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('note', models.TextField()),
                ('to_title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('attach_document', models.FileField(blank=True, null=True, upload_to='static/postal/receive')),
            ],
        ),
    ]
