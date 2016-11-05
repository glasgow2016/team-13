from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Centre (models.Model):
	ID = models.AutoField(primary_key=True)
	location = models.CharField(default = '', max_length=100)
	region = models.CharField(default = '', max_length=100)

class VisitType (models.Model):
	ID = models.AutoField(primary_key = True)
	visitType = models.CharField(default = '', max_length = 100)

class JourneyStage (models.Model):
	ID = models.AutoField(primary_key = True)
	joureyStage = models.CharField(default = '', max_length = 100)

class NatureOfVisit (models.Model):
	ID = models.AutoField(primary_key = True)
	natureOfVisit = models.CharField(default = '', max_length = 100)

class CancerSite (models.Model):
	ID = models.AutoField(primary_key = True)
	cancerSite = models.CharField(default = '', max_length = 100)

class Activity (models.Model):
	ID = models.AutoField(primary_key=True)
	name = models.CharField(default = '', max_length = 50)
	category = models.CharField(default = '', max_length = 50)
	isCore = models.BooleanField(default=True)

class Activity_Record (models.Model):
	ID = models.AutoField(primary_key = True)
	activity = models.IntegerField(default = 0)
	record = models.IntegerField(default = 0)
	timeStamp = models.DateTimeField()

class StaffMember_Record (models.Model):
	ID = models.AutoField(primary_key = True)
	staffMember = models.CharField(default = '', max_length = 50)
	record = models.IntegerField(default = 0)
	timeStamp = models.DateTimeField()

class Gender (models.Model):
	ID = models.AutoField(primary_key = True)
	gender = models.CharField(default = '', max_length = 50)

class Age (models.Model):
	ID = models.AutoField(primary_key = True)
	age = models.CharField(default = '', max_length = 50)

class Person (models.Model):
	ID = models.AutoField(primary_key=True)
	person = models.CharField(default = '', max_length=50)

class StaffGroup (models.Model):
	ID = models.AutoField(primary_key=True)
	staffGroup = models.CharField(default = '', max_length = 50)

class StaffMember (models.Model):
	name = models.CharField(default = '', max_length = 50)
	username = models.CharField(default = '', max_length = 50)
	password = models.CharField(default = '', max_length = 50)
	email = models.CharField(default = '', primary_key=True, max_length = 50)
	staffGroup = models.CharField(default = '', max_length = 50)
	centre = Centre()

class Record (models.Model):
	ID = models.AutoField(primary_key = True)
	timeStamp = models.DateTimeField()
	gender = Gender()
	age = Age()
	person = Person()
	visitType = VisitType()
	journeyStage = JourneyStage()
	natureOfVisit = NatureOfVisit()
	cancerSite = CancerSite()