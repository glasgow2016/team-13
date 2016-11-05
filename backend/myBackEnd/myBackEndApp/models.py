from __future__ import unicode_literals

from django.db import models


class Activity(models.Model):
    name = models.CharField(default='', max_length=50)
    category = models.CharField(default='', max_length=50)
    isCore = models.BooleanField(default=True)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class StaffMember (models.Model):
    name = models.CharField(default='', max_length=50)
    username = models.CharField(default='', max_length=50)
    password = models.CharField(default='', max_length=50)
    email = models.CharField(default='', primary_key=True, max_length=50)
    staffGroup = models.CharField(default='', max_length=50)
    location = models.CharField(default='', max_length=100)
    region = models.CharField(default='', max_length=100)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class Record (models.Model):
    timeStamp = models.DateTimeField()
    gender = models.CharField(default='', max_length=50)
    age = models.IntegerField(default = 0)
    person = models.CharField(default='', max_length=50)
    visitType = models.CharField(default='', max_length=100)
    journeyStage = models.CharField(default='', max_length=100)
    natureOfVisit = models.CharField(default='', max_length=100)
    cancerSite = models.CharField(default='', max_length=100)
