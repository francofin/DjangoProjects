# Generated by Django 4.0.4 on 2022-07-15 04:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='education_detail',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='industry_detail',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='address',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='education',
            field=models.CharField(choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Phd', 'Phd'), ('Certificate', 'Certificate')], default='Bachelors', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='email',
            field=models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='job',
            name='industry',
            field=models.CharField(choices=[('Business', 'Business'), ('Information Technology', 'It'), ('Banking', 'Banking'), ('Marketing', 'Marketing'), ('Energy', 'Energy'), ('Sales', 'Sales'), ('Education/Training', 'Education'), ('Telecommunication', 'Telecommunication'), ('Retail', 'Retail'), ('Others', 'Others')], default='Business', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobType',
            field=models.CharField(choices=[('Permanent', 'Permanent'), ('Contract', 'Temporary'), ('Internship', 'Internship'), ('Volunteer', 'Volunteer')], default='Permanent', max_length=50),
        ),
    ]
