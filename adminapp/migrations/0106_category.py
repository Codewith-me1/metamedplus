# Generated by Django 4.2.5 on 2023-10-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0105_alter_party_opening_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]