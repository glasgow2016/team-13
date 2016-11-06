from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import *
import json
import csv
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


# def add_data(request):
#     print(len(Record.objects.filter(activity__isCore=True)))
#     # for i in range(len(data)):
#     #     d = data[i]
#     #     date = "2016-11-05 " + str(i%24) + ":30:30"
#     #     record = Record(location="Glasgow", region="Scotland", timeStamp=date,seenBy=d["seenBy"], person=d["person"], visitType=d["visitType"], gender=d["gender"], age=d["age"], cancerSite=d["cancerSite"], journeyStage=d["journeySite"], natureOfVisit=d["natureOfVisit"])
#     #     record.save()
#     return HttpResponse("OK")

def create_report(request):

    data = {"day1": 1,
            "day2": 2}

    new_pwc = Record.objects.filter(person="PwC", visitType="New")
    new_carer = Record.objects.filter(person="Carer", visitType="New")

    new_pwc_number_d1 = 0
    new_pwc_number_d2 = 0
    day1 = data["day1"]
    day2 = data["day2"]
    for np in new_pwc:
        if int(str(np.timeStamp)[9:10]) == day1:
            new_pwc_number_d1 = new_pwc_number_d1 + 1
        elif int(str(np.timeStamp)[9:10]) == day2:
            new_pwc_number_d2 = new_pwc_number_d2 + 1
    
    new_carer_number_d1 = 0
    new_carer_number_d2 = 0
    for nc in new_carer:
        if int(str(nc.timeStamp)[9:10]) == day1:
            new_carer_number_d1 = new_carer_number_d1 + 1
        elif int(str(np.timeStamp)[9:10]) == day2:
            new_carer_number_d2 = new_carer_number_d2 + 1

    records = Record.objects.all()

    total_visits_d1 = 0
    total_visits_d2 = 0
    for r in records:
        if int(str(r.timeStamp)[9:10]) == day1:
            total_visits_d1 = total_visits_d1 + 1
        elif int(str(r.timeStamp)[9:10]) == day2:
            total_visits_d2 = total_visits_d2 + 1

    return JsonResponse({"New_PwC_day1" : new_pwc_number_d1,
                         "New_PwC_day2" : new_pwc_number_d2,
                         "New_Carer_day1" : new_carer_number_d1,
                         "New_Carer_day2" : new_carer_number_d2,
                         "Total_Visits_d1" : total_visits_d1,
                         "Total_Visits_d2" : total_visits_d2})