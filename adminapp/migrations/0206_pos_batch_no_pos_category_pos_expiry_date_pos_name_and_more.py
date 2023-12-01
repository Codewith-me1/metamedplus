# Generated by Django 4.1.2 on 2023-12-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0205_brs'),
    ]

    operations = [
        migrations.AddField(
            model_name='pos',
            name='batch_no',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='pos',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pos',
            name='expiry_date',
            field=models.DecimalField(decimal_places=3, max_digits=13, null=True),
        ),
        migrations.AddField(
            model_name='pos',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pos',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=13, null=True),
        ),
        migrations.AddField(
            model_name='pos',
            name='qty',
            field=models.DecimalField(decimal_places=3, max_digits=13, null=True),
        ),
        migrations.AddField(
            model_name='pos',
            name='tax',
            field=models.DecimalField(decimal_places=3, max_digits=13, null=True),
        ),
        migrations.AddField(
            model_name='pos',
            name='total',
            field=models.DecimalField(decimal_places=3, max_digits=13, null=True),
        ),
    ]
