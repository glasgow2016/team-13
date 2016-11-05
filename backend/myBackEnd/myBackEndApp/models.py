from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StaffMember (models.Model):
	name = models.CharField(default = '', max_length = 50)
	username = models.CharField(default = '', max_length = 50)
	password = models.CharField(default = '', max_length = 50)
	email = models.CharField(default = '', primary_key=True, max_length = 50)
	staffGroup = models.CharField(default = '', max_length = 50)
	centreLocation = models.CharField(default = '', max_length = 50)
	def __init__(self):
		return self.name

class VisitType (models.Model):
	vType = models.CharField(default = '', max_length = 100)

class VisitorType (models.Model):
	vType = models.CharField(default = '', max_length = 100)

class JourneyStage (models.Model):
	stage = models.CharField(default = '', max_length = 100)

class VisitNature (models.Model):
	nature = models.CharField(default = '', max_length = 100)

class CancerSite (models.Model):
	site = models.CharField(default = '', max_length = 100)

class Activity (models.Model):
	activityID = models.AutoField(primary_key=True)
	name = models.CharField(default = '', max_length = 50)
	category = models.CharField(default = '', max_length = 50)
	activityType = models.BooleanField(default=True)
	def __init__(self):
		return self.name

class Activity_Record (models.Model):
	activityID = models.IntegerField(default = 0)
	recordID = models.IntegerField(default = 0)
	timeStamp = models.DateTimeField()

class StaffMember_Record (models.Model):
	staffMember = models.CharField(default = '', max_length = 50)
	recordID = models.IntegerField(default = 0)
	timeStamp = models.DateTimeField()


class Record (models.Model):
	recordID = models.AutoField(primary_key = True)
	timeStamp = models.DateTimeField()
	gender = models.CharField(default = '', max_length = 50)
	visitType = VisitType()
	visitorType = VisitorType()
	journeyStage = JourneyStage()
	visitNature = VisitNature()
	site = CancerSite()







