from django.conf.urls import url
from androidServApp import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^newEmployee', views.newEmployee, name = 'newEmployee'),
	url(r'^newProject', views.newProject, name = 'newProject'),
]