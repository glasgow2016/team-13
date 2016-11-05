from django.shortcuts import render
import datetime

from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here

def index(request):
	return render(request, "index.html")

def index(request):
    return render(request, "index.html")
def login(request):
	userData = json.loads(request.body)

	username = userData["username"]
	password = userData["password"]

	user = StaffMember.objects.get(username = username)

	if user.password == password:
		return JsonResponse({"Status" : "Success",
							 "email" : user.email})
	else:
		return JsonResponse({"Status" : "Fail"})


def save_entry(request):
    """This is what we get in the post request:
    Person;person
    Visit Type;visit_type
    Gender;gender
    Age;age
    Cancer Site;cancer_site
    Journey Stage;journey_stage
    Nature of Visit;nature_of_visit
    1st Activity;activity[]
    2nd Activity;activity[]
    3rd Activity;activity[]
    """
    if request.method == 'POST':
        visit_type = VisitType(visitType=request.body['visit_type'])
        person = Person(person=request.body['person'])
        gender = Gender(gender=request.body['gender'])
        age = Age(age=request.body['age'])
        cancer_site = CancerSite(cancerSite=request.body['cancer_site'])
        journey_stage = JourneyStage(joureyStage=request.body['journey_stage'])
        nature_of_visit = NatureOfVisit(natureOfVisit=request.body['nature_of_visit'])
        activities = request.body['activity']  # this is []
        # save all the above as new objects in the db
        visit_type.save()
        person.save()
        gender.save()
        age.save()
        cancer_site.save()
        journey_stage.save()
        nature_of_visit.save()
        record = Record(timeStamp=datetime.datetime.now(),
                        gender=gender,
                        age=age,
                        person=person,
                        visitType=visit_type,
                        journeyStage=journey_stage,
                        natureOfVisit=nature_of_visit,
                        cancerSite=cancer_site)


#
#
# class Activity (models.Model):
# 	id = models.AutoField(primary_key=True)
# 	name = models.CharField(default = '', max_length = 50)
# 	category = models.CharField(default = '', max_length = 50)
# 	isCore = models.BooleanField(default=True)
# 	def __init__(self):
# 		return self.name
#
# class Activity_Record (models.Model):
# 	id = models.AutoField(primary_key = True)
# 	activity = models.IntegerField(default = 0)
# 	record = models.IntegerField(default = 0)
# 	timeStamp = models.DateTimeField()
