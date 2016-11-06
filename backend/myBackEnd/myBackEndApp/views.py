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
        # print("fdgdfg?fdgfdgfdgfdgdfgfdgdf")
        print(request.POST)

        data = json.loads(request.body.decode("utf-8"))
        record = Record(timeStamp=datetime.now(),
                        gender=data['gender'],
                        age=data['age'],
                        person=data['person'],
                        visitType=data['visit_type'],
                        journeyStage=data['journey_stage'],
                        natureOfVisit=data['nature_of_visit'],
                        cancerSite=data['cancer_site'])
        record.save()
        # activities = [{"category": "abc", "isCore": True, "name": "dsfd"}]
        for e in data['activities']:
            a = Activity(name=e['name'],
                         isCore=e['isCore'],
                         category=e['category'],
                         record=record)
            a.save()
        return HttpResponse()
    else:
        return render(request, "index.html")


def plots(request):
    print('Number of records with at least one core activity:')
    print(len(Record.objects.filter(activity__isCore=True)))
    print('Number of records with at least one non-core activity:')
    print(len(Record.objects.filter(activity__isCore=False)))
    return HttpResponse()

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
"location": "Bratislava",
"activities":[{"category": "abc", "isCore": true, "name": "dsfd"},{"category": "abc", "isCore": false, "name": "dsfd"}]
}
"""
"""
New Record:
r = Record(gender='woman', age=55, person='sf',visitType='sserios',journeyStage='new',natureOfVisit='confidential',cancerSite='heaetr')
r.save()
Activity(name='exercise1', category='abc', isCore=True, record=r).save()

Sample querying of ForeignKeys:
# at least one case where isCore is true
Record.objects.filter(activity__isCore=True)
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
