# Generated by Django 4.0.4 on 2022-09-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]