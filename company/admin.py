from django.contrib import admin
from .models import Department, Staff, Project
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'depart')


class DepartAdmin(admin.ModelAdmin):
    list_display = ('depart_name', 'number_staff')


admin.site.register(Department, DepartAdmin)
admin.site.register(Project)
admin.site.register(Staff, AuthorAdmin)
