from django.db import models
import datetime

class Employee(models.Model):
	name = models.CharField(max_length=128)
	email = models.EmailField()
	password = models.CharField(max_length=128)
	designation = models.CharField(max_length=128)
	department = models.CharField(max_length=128)
	company = models.CharField(max_length=128)
	ismanager = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Project(models.Model):
	pname = models.CharField(max_length=128)
	description = models.CharField(max_length=1000)
	startDate = models.DateField(default=datetime.date.today)

	def __str__(self):
		return self.pname

class ProjectManagerRelation(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	manager = models.ForeignKey(Employee, on_delete=models.CASCADE)

	def __str__(self):
		return self.project.pname + " " + self.manager.name

class ProjectEmployeeRelation(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)

	def __str__(self):
		return self.project.pname + " " + self.employee.name