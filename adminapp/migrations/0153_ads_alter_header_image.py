# Generated by Django 4.2.5 on 2023-10-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0152_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads', models.ImageField(upload_to='static/ads')),
            ],
        ),
        migrations.AlterField(
            model_name='header',
            name='image',
            field=models.ImageField(upload_to='static/cms'),
        ),
    ]
