# Generated by Django 4.0.4 on 2022-08-25 02:58

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_about_remove_customuser_about1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cover_picture',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture10',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture11',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True, verbose_name='profile_picture11'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture12',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture7',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture8',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture9',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True, verbose_name='profile_picture9'),
        ),
    ]
