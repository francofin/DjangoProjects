# Generated by Django 4.0.4 on 2022-09-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockuploader', '0002_sp500_cik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sp500',
            name='cik',
            field=models.CharField(blank=True, default=None, max_length=400, null=True),
        ),
    ]