from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here


@csrf_exempt
def index(request):
    # we just save the record without the activities for now
    if request.method == 'POST':
        record = Record(timeStamp=datetime.now(),
                        gender=request.body['gender'],
                        age=request.body['age'],
                        person=request.body['person'],
                        visitType=request.body['visit_type'],
                        journeyStage=request.body['journey_stage'],
                        natureOfVisit=request.body['nature_of_visit'],
                        cancerSite=request.body['cancer_site'])
        record.save()
        # activities = [{"category": "abc", "isCore": True, "name": "dsfd"}]
        for e in request.body['activities']:
            a = Activity(name=e['name'],
                         isCore=e['isCore'],
                         category=e['category'],
                         record=record)
            a.save()
    else:
        return render(request, "index.html")


"""
{
"gender":"man",
"age":33,
"person":"a",
"visit_type":"b",
"journey_stage":"Starting",
"nature_of_visit":"DropIn",
"cancer_site":"Brain",
"region": "usa",
"location": "Bratislava"
"activities":[{"category": "abc", "isCore": True, "name": "dsfd"},{"category": "abc", "isCore": False, "name": "dsfd"}]
}
"""


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
