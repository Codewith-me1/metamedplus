# Generated by Django 4.1.2 on 2023-12-02 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0210_party_account_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=13)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.asset')),
            ],
        ),
    ]
