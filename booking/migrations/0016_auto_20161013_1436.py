# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-13 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_auto_20161013_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingroom',
            name='status',
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('wn', 'Oczekuje na potwierdzenie, Nieop\u0142acony'), ('rn', 'Potwierdzona rezerwacja, Nieop\u0142acony'), ('wp', 'Oczekuje na potwierdzenie, Op\u0142acony'), ('rp', 'Potwierdzona rezerwacja, Op\u0142acony')], default='wn', max_length=4, verbose_name='Status rezerwacji'),
        ),
    ]
