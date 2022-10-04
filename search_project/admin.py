from django.contrib import admin
from .models import Project, DevTechnology
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(DevTechnology)
class DevTechnologyAdmin(admin.ModelAdmin):
    pass