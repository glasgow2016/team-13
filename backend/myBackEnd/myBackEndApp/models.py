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
	id = models.AutoField(primary_key = True)
	visitType = models.CharField(default = '', max_length = 100)

class VisitorType (models.Model):
	id = models.AutoField(primary_key = True)
	visitorType = models.CharField(default = '', max_length = 100)

class JourneyStage (models.Model):
	id = models.AutoField(primary_key = True)
	joureyStage = models.CharField(default = '', max_length = 100)

class NatureOfVisit (models.Model):
	id = models.AutoField(primary_key = True)
	natureOfVisit = models.CharField(default = '', max_length = 100)

class CancerSite (models.Model):
	id = models.AutoField(primary_key = True)
	cancerSite = models.CharField(default = '', max_length = 100)

class Activity (models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(default = '', max_length = 50)
	category = models.CharField(default = '', max_length = 50)
	isCore = models.BooleanField(default=True)
	def __init__(self):
		return self.name

class Activity_Record (models.Model):
	id = models.AutoField(primary_key = True)
	activity = models.IntegerField(default = 0)
	record = models.IntegerField(default = 0)
	timeStamp = models.DateTimeField()

class StaffMember_Record (models.Model):
	id = models.AutoField(primary_key = True)
	staffMember = models.CharField(default = '', max_length = 50)
	record = models.IntegerField(default = 0)
	timeStamp = models.DateTimeField()

class Gender (models.Model):
	id = models.AutoField(primary_key = True)
	gender = models.CharField(default = '', max_length = 50)

class Age (models.Model):
	id = models.AutoField(primary_key = True)
	age = models.CharField(default = '', max_length = 50)

class Record (models.Model):
	id = models.AutoField(primary_key = True)
	timeStamp = models.DateTimeField()
	gender = Gender()
	age = Age()
	visitType = VisitType()
	visitorType = VisitorType()
	journeyStage = JourneyStage()
	natureOfVisit = NatureOfVisit()
	cancerSite = CancerSite()