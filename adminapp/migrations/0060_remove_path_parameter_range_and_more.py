# Generated by Django 4.2.5 on 2023-09-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0059_remove_path_category_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='path_parameter',
            name='range',
        ),
        migrations.AddField(
            model_name='path_parameter',
            name='reference_range',
            field=models.CharField(default='test', max_length=255),
        ),
        migrations.AlterField(
            model_name='path_parameter',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='path_parameter',
            name='parameter_name',
            field=models.CharField(default='test', max_length=255),
        ),
        migrations.AlterField(
            model_name='path_parameter',
            name='unit',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
