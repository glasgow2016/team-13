# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBackEndApp', '0006_auto_20161105_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='gender',
        ),
    ]