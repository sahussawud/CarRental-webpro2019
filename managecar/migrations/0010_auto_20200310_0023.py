# Generated by Django 3.0.3 on 2020-03-09 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managecar', '0009_delete_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rent',
            old_name='car',
            new_name='car_id',
        ),
        migrations.RenameField(
            model_name='rent',
            old_name='renter',
            new_name='customer_id',
        ),
    ]
