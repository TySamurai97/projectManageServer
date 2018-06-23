from django.contrib import admin
from androidServApp.models import ProjectEmployeeRelation, ProjectManagerRelation, Employee, Project

# Register your models here.
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(ProjectManagerRelation)
admin.site.register(ProjectEmployeeRelation)