# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_booking_overall_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='overall_price',
            field=models.PositiveIntegerField(null=True, verbose_name='Cena za ca\u0142y pobyt'),
        ),
    ]
