# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 15:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20160831_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ('-reservation_date',), 'verbose_name': 'Rezerwacje', 'verbose_name_plural': 'Rezerwacje'},
        ),
        migrations.AlterModelOptions(
            name='bookingroom',
            options={'verbose_name': 'Pok\xf3j', 'verbose_name_plural': 'Pokoje'},
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 31, 17, 58, 33, 97072), verbose_name='Data dokonania rezerwacji.'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_from',
            field=models.DateField(verbose_name='Rezerwacja od'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_to',
            field=models.DateField(verbose_name='Rezerwacja do'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='overall_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Cena za ca\u0142y pobyt'),
        ),
    ]
