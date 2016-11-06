from django.conf.urls import  include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^activities/$', views.activities, name='activities'),
	url(r'^create_report/$', views.create_report, name='create_report'),
    url(r'^query_DB/$', views.query_DB, name='query_DB')

	url(r'^plots/$', views.plots, name='plots'),
	url(r'^query_DB/$', views.query_DB, name='query_DB'),
	url(r'^thankyou/$', views.thankyou, name='thankyou'),
	url(r'^report/$', views.report, name='report'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
