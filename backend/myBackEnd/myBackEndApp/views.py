from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
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


