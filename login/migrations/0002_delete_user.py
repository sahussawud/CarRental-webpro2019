# Generated by Django 3.0.3 on 2020-03-07 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managecar', '0002_auto_20200307_1552'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
