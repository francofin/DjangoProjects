# Generated by Django 4.0.4 on 2022-12-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockuploader', '0018_etf_universe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
