import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','schedulingServer.settings')
import django
django.setup()

from androidServApp.models import Employee, Project, ProjectManagerRelation, ProjectEmployeeRelation

def addEmployee(name, email, password, designation, department, company, ismanager):
	entry, done = Employee.objects.get_or_create(name = name, email = email, password = password, designation = designation, department = department, company = company, ismanager = ismanager)
	entry.save()
	return entry, done

def addProject(pname, description, startDate):
	entry, done = Project.objects.get_or_create(pname = pname, description = description, startDate = startDate)
	entry.save()
	return entry, done

def addProjectManagerRelation(project, manager):
	entry, done = ProjectManagerRelation.objects.get_or_create(project = project, manager = manager)
	entry.save()
	return entry, done

def addProjectEmployeeRelation(project, employee):
	entry, done = ProjectEmployeeRelation.objects.get_or_create(employee = employee, project = project)
	entry.save()
	return entry, done

if __name__ == '__main__':
	emp = addEmployee("Tanay Saxena","tyjackx@gmail.com","pass","SSDE","A","Amazon",1)[0]
	proj = addProject("blacksite", "asdfghjklmnbvcxz", "2018-05-06")[0]
	addProjectEmployeeRelation(proj, emp)
	addProjectManagerRelation(proj, emp)
