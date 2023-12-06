from django.contrib import admin
from projectsapp.models import Project 

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)

