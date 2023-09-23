# Generated by Django 4.2.5 on 2023-09-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_role_remove_staff_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=100, unique=True)),
                ('role', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('specialist', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=20)),
                ('blood_group', models.CharField(max_length=5)),
                ('date_of_birth', models.DateField()),
                ('date_of_joining', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('emergency_contact', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff_photos/')),
                ('current_address', models.TextField(blank=True, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('qualification', models.TextField(blank=True, null=True)),
                ('work_experience', models.TextField(blank=True, null=True)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=20, null=True)),
                ('national_id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('local_id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('payroll', models.CharField(blank=True, max_length=100, null=True)),
                ('epf_no', models.CharField(blank=True, max_length=20, null=True)),
                ('basic_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('contract_type', models.CharField(blank=True, max_length=100, null=True)),
                ('work_shift', models.CharField(blank=True, max_length=100, null=True)),
                ('work_location', models.CharField(blank=True, max_length=100, null=True)),
                ('paid_leave', models.BooleanField(default=False)),
                ('number_of_leaves', models.PositiveIntegerField(blank=True, null=True)),
                ('account_title', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_no', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_branch_name', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='staff_documents/')),
                ('joining_letter', models.FileField(blank=True, null=True, upload_to='staff_documents/')),
                ('other_documents', models.FileField(blank=True, null=True, upload_to='staff_documents/')),
            ],
        ),
    ]
