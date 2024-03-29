# Generated by Django 4.0.4 on 2022-08-20 17:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture1',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_picture1'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture2',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_picture2'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture3',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_picture3'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture4',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_picture4'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture5',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_picture5'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture6',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_picture6'),
        ),
    ]
