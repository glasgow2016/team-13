from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here

def post(request):
	string = "FSG Bereavement;Facilitated Support Groups;1[FSG Family and Friends;Facilitated Support Groups;1[FSG General;Facilitated Support Groups;1[FSG Men's;Facilitated Support Groups;1[FSG Secondary Cancer;Facilitated Support Groups;1[FSG Young Person's;Facilitated Support Groups;1[FSG Young Women's;Facilitated Support Groups;1[NG Brain;Networking Group;1[NG Breast;Networking Group;1[NG Gynae;Networking Group;1[NG Haematology;Networking Group;1[NG Head/Neck;Networking Group;1[NG Laryngectomy;Networking Group;1[NG Lower GI;Networking Group;1[NG Lung;Networking Group;1[NG Lymphoedema;Networking Group;1[NG Myeloma;Networking Group;1[NG Prostate;Networking Group;1[NG Rare;Networking Group;1[NG Sarcoma;Networking Group;1[NG Upper GI;Networking Group;1[Psych Support - Couple;Psychological Support;1[Psych Support - Family;Psychological Support;1[Psych Support - Individual;Psychological Support;1[Benefits - Couple;Benefits Advice;1[Benefits - Family;Benefits Advice;1[Benefits - Individual;Benefits Advice;1[Benefits Workshop;C&W;1[Caring for Someone with Cancer;C&W;1[enetics;C&W;1[Getting Started with Cancer Treatment;C&W;1[Kids Days;C&W;1[Lecture Series;C&W;1[Look Good Feel Better;C&W;1[Managing Stress;C&W;1[Talking Heads: Managing Hair Loss;C&W;1[Where Now?;C&W;1[Creative Writing;Sessional;1[Expressive art;Sessional;1[Nutrition;Sessional;1[Relaxation;Sessional;1[Tai Chi/Qi Gong;Sessional;1[Yoga;Sessional;1[Auricular Acupuncture;Additional;0[Bereavement Course;Additional;0[Cancer in the Workplace;Additional;0[Fatigue Management;Additional;0[Gardening;Additional;0[Gentle Exercise;Additional;0[Introduction to Radiotherapy;Additional;0[Living With and Beyond Prostate Cancer;Additional;0[Meditation;Additional;0[Mind over Mood;Additional;0[Mindfulness;Additional;0[Music Therapy/Choir;Additional;0[Nordic Walking;Additional;0[Pilates;Additional;0[Prosthesis;Additional;0[Scrapbooking;Additional;0[Sleep;Additional;0"
	list = string.split("[")
	for l in list:
		lst = l.split(";")
		act = Activity(name=lst[0], category=lst[1], isCore=lst[2])
		act.save()

	return HttpResponse("OK")