# Generated by Django 3.0.3 on 2020-03-07 09:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managecar', '0002_auto_20200307_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='renter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
