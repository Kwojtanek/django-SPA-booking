# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20160829_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingperson',
            name='identification_number',
            field=models.CharField(blank=True, max_length=32, verbose_name='Nr. dowodu/PESEL'),
        ),
    ]
