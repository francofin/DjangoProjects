# Generated by Django 4.0.4 on 2022-09-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockuploader', '0013_eurostock_universe_nasdaq_universe_sp500_universe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='universe',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
