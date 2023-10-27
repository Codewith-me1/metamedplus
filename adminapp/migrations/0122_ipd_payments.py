# Generated by Django 4.2.5 on 2023-10-12 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0121_ipd_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ipd_Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_mode', models.CharField(max_length=10)),
                ('note', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.patient')),
            ],
        ),
    ]