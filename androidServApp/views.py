from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from populate import addEmployee, addProject, addProjectEmployeeRelation, addProjectManagerRelation

def index(request):
	return HttpResponse("ma homie !!!!!")

# http://127.0.0.1:8000/androidServApp/newEmployee?name=Tanay Saxena&email=tyjackx@gmail.com&pass=pass&des=SSDE&dept=A&company=Amazon&ismanager=1

def newEmployee(request):
	name = request.GET.get('name')
	email = request.GET.get('email')
	password = request.GET.get('pass')
	designation = request.GET.get('des')
	department = request.GET.get('dept')
	company = request.GET.get('company')
	ismanager = request.GET.get('ismanager')

	done = False
	if( name is not None and email is not None and password is not None and designation is not None and department is not None and company is not None and ismanager is not None):
		entry, done = addEmployee(name, email, password, designation, department, company, ismanager)
	return HttpResponse(json.dumps({'result':done}), content_type="application/json")

# http://127.0.0.1:8000/androidServApp/newProject?pname=blacksite&desc=asdfghjk&stdate=2018-05-06

def newProject(request):
	pname = request.GET.get('pname')
	description = request.GET.get('desc')
	startDate = request.GET.get('stdate')
	done = False
	if( pname is not None and description is not None and startDate is not None):
		entry, done = addProject(pname, description, startDate)
	return HttpResponse(json.dumps({'result':done}), content_type="application/json")
