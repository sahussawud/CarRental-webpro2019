# Generated by Django 3.0.3 on 2020-02-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('years', models.CharField(max_length=4)),
                ('color', models.CharField(choices=[('BLUE', 'น้ำเงิน'), ('RED', 'แดง'), ('PINK', 'ชมพู'), ('ORA', 'ส้ม'), ('BLA', 'ดำ'), ('WHI', 'ขาว'), ('SIL', 'เงิน'), ('BRO', 'บรอนซ์'), ('YEL', 'เหลือง')], max_length=4)),
                ('category', models.CharField(choices=[('SUV', 'Sport Utility Vehicle'), ('PPV', 'Pick-Up Passenger Vehicle'), ('MPV', 'Multi Purpose Vehicle'), ('ECO', 'Eco Car'), ('HEV', 'Hybrid Electric Vehicles'), ('EV', 'Electric Vehicles'), ('PU', 'Pick-Up Truck'), ('VAN', 'Van Car')], max_length=3)),
                ('type_gear', models.CharField(choices=[('AUT', 'เกียร์ธรรมดา'), ('MAN', 'เกียร์อัตโนมัติ'), ('CBT', 'เกียร์ CVT'), ('DTC', 'เกียร์กึ่งอัตโนมัติ และ เกียร์คลัตช์คู่ DCT')], max_length=3)),
                ('number_seat', models.SmallIntegerField()),
                ('number_door', models.SmallIntegerField()),
                ('status', models.CharField(choices=[('AV', 'Available'), ('NO', 'Not Available'), ('HI', 'Hide')], max_length=2)),
                ('price', models.FloatField()),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic_url', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('P', 'Picked'), ('A', 'Approved'), ('D', 'Denied'), ('R', 'Return')], max_length=1)),
                ('total_price', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('car', models.ManyToManyField(to='managecar.Car')),
                ('renter', models.ManyToManyField(to='login.User')),
            ],
        ),
    ]
