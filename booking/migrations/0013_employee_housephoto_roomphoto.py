# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 22:34
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('booking', '0012_booking_additional_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HousePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'', verbose_name='Zdj\u0119cie')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='booking.BookingHouse', verbose_name='pok\xf3j')),
            ],
            options={
                'verbose_name': 'Zdj\u0119cie budynku',
                'verbose_name_plural': 'Zdj\u0119cia budynku',
            },
        ),
        migrations.CreateModel(
            name='RoomPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'', verbose_name='Zdj\u0119cie')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='booking.BookingRoom', verbose_name='pok\xf3j')),
            ],
            options={
                'verbose_name': 'Zdj\u0119cie pokoju',
                'verbose_name_plural': 'Zdj\u0119cia pokoju',
            },
        ),
    ]