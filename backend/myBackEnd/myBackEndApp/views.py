from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here

def index(request):
	return render(request, "index.html")

def post(request):
	
	return HttpResponse("OK")
