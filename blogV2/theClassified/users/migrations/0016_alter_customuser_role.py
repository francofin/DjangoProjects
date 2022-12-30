# Generated by Django 4.0.4 on 2022-12-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_userprofile_store_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Subscriber', 'Subscriber'), ('Seller', 'Seller'), ('Admin', 'Admin'), ('Employee', 'Employee'), ('Client', 'Client'), ('Investor', 'Investor')], default='Subscriber', max_length=300),
        ),
    ]
