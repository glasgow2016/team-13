from django.conf.urls import  include, url
from django.contrib import admin
from . import views

urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^activities/$', views.activities, name='activities')
	# url(r'^runscript/$', views.runscript, name='runscript')

]