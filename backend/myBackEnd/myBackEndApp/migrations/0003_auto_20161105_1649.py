# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBackEndApp', '0002_auto_20161105_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='type',
            new_name='isCore',
        ),
        migrations.RenameField(
            model_name='cancersite',
            old_name='site',
            new_name='cancerSite',
        ),
        migrations.RenameField(
            model_name='journeystage',
            old_name='stage',
            new_name='joureyStage',
        ),
        migrations.RenameField(
            model_name='visitortype',
            old_name='vType',
            new_name='visitorType',
        ),
        migrations.RenameField(
            model_name='visittype',
            old_name='vType',
            new_name='visitType',
        ),
    ]
