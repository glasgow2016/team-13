from django.conf.urls import  include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^activities/$', views.activities, name='activities'),
    url(r'^plots/$', views.plots, name='plots')
	# url(r'^runscript/$', views.runscript, name='runscript')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
