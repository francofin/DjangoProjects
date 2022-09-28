# Generated by Django 4.0.4 on 2022-09-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockuploader', '0012_eurostock'),
    ]

    operations = [
        migrations.AddField(
            model_name='eurostock',
            name='universe',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='nasdaq',
            name='universe',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sp500',
            name='universe',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tsx',
            name='universe',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]