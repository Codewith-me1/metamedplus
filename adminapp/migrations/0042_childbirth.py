# Generated by Django 4.2.5 on 2023-09-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0041_tpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildBirth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('child_photo', models.ImageField(blank=True, null=True, upload_to='Birth/child_photos/')),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('case_id', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_photo', models.ImageField(blank=True, null=True, upload_to='Birth/mother_photo/')),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_photo', models.ImageField(blank=True, null=True, upload_to='Birth/father_photo/')),
                ('report', models.TextField()),
                ('document_photo', models.ImageField(blank=True, null=True, upload_to='Birth/document_photos/')),
            ],
        ),
    ]