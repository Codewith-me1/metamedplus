# Generated by Django 4.1.2 on 2023-11-26 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0193_pos_alter_payroll_date_pos_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation_Assistants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistant', models.CharField(max_length=20)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.operation')),
            ],
        ),
        migrations.DeleteModel(
            name='Pos_item',
        ),
    ]
