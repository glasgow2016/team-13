# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBackEndApp', '0009_auto_20161106_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='seenBy',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='age',
            field=models.CharField(default='', max_length=50),
        ),
    ]
