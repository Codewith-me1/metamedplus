# Generated by Django 4.2.5 on 2023-09-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0080_purchase_delete_purchase_med'),
    ]

    operations = [
        migrations.CreateModel(
            name='NursingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('nurse', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
    ]