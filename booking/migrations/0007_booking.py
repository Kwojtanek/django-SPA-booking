# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20160831_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('booking_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_person', to='booking.BookingPerson', verbose_name='Rezerwuj\u0105cy')),
                ('booking_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_room', to='booking.BookingRoom', verbose_name='Pok\xf3j')),
            ],
        ),
    ]
