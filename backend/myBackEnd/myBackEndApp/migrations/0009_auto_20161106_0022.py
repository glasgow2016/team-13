# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBackEndApp', '0008_auto_20161105_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='region',
            field=models.CharField(default='', max_length=100),
        ),
    ]
