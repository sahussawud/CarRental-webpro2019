# Generated by Django 3.0.3 on 2020-03-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managecar', '0016_auto_20200310_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=20),
        ),
    ]
