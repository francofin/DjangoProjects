# Generated by Django 4.0.4 on 2022-08-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Subscriber', 'Subscriber'), ('Seller', 'Seller'), ('Admin', 'Admin'), ('Employee', 'Employee'), ('Client', 'Role')], default='Subscriber', max_length=300),
        ),
    ]
