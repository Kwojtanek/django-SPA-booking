# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type', models.CharField(choices=[('Pensjonat', 'Pensjonat'), ('Kemping', 'Kemping'), ('Pole biwakowe', 'Pole biwakowe'), ('Dom wycieczkowy', 'Dom wycieczkowy'), ('Hotel', 'Hotel'), ('Motel', 'Motel'), ('Schronisko', 'Schronisko'), ('Inny obiekt', 'Inny obiekt')], max_length=128, verbose_name='Rodzaj obiektu')),
                ('name', models.CharField(max_length=128, verbose_name='Nazwa obiektu')),
                ('street', models.CharField(max_length=128, verbose_name='Ulica')),
                ('street_nr', models.CharField(max_length=64, verbose_name='Numer domu')),
                ('city', models.CharField(max_length=128, verbose_name='Miejscowo\u015b\u0107')),
                ('additional_info', models.TextField(blank=True, verbose_name='Dodatkowe informacje')),
            ],
        ),
    ]
