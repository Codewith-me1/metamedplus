# Generated by Django 4.2.5 on 2023-09-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0043_deathrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
