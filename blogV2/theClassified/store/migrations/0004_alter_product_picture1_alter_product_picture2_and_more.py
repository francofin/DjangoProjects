# Generated by Django 4.0.4 on 2022-09-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_store_products_store_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture1',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture2',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture3',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture4',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture5',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture6',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture7',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='picture1',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='picture2',
            field=models.CharField(blank=True, default=None, max_length=600, null=True),
        ),
    ]
