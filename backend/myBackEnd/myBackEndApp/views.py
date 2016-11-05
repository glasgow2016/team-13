from django.shortcuts import render
import datetime

from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here


def index(request):
    return render(request, "index.html")


def save_request(request):
    # we just save the record without the activities for now
    if request.method == 'POST':
        record = Record(timeStamp=datetime.datetime.now(),
                        gender=gender=request.body['gender'],
                        age=request.body['age'],
                        person=request.body['person'],
                        visitType=request.body['visit_type'],
                        journeyStage=request.body['journey_stage'],
                        natureOfVisit=request.body['nature_of_visit'],
                        cancerSite=request.body['cancer_site'])
        record.save()


def login(request):
    userData = json.loads(request.body)
    username = userData["username"]
    password = userData["password"]
    user = StaffMember.objects.get(username=username)
    if user.password == password:
        return JsonResponse({"Status": "Success",
                             "email": user.email})
    else:
        return JsonResponse({"Status": "Fail"})


def activities(request):
    activities = Activity.objects.all()
    activities_list = []
    for activity in activities:
        activities_list.append({"name": activity.name,
                                "category": activity.category,
                                "isCore": activity.isCore})

    return JsonResponse({"activities": activities_list})
