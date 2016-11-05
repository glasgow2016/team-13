from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here

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

def activities(request):
	activities = Activity.objects.all()
	
	activities_list = []
	for activity in activities:
		activities_list.append({"name": activity.name,
								"category": activity.category,
								"isCore": activity.isCore})
				
	return JsonResponse({"activities": activities_list})

# def runscript(request):

# 	gender = Gender.objects.first()

# 	print gender.gender

# 	record = Record(gender=gender)
# 	record.save()

# 	return HttpResponse("ok")