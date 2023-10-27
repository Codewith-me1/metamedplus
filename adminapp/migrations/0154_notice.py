# Generated by Django 4.2.5 on 2023-10-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0153_ads_alter_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]