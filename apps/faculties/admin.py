from django.contrib import admin
from .models import Faculty, Department, Teacher


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'dean', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'head', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['faculty']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'department', 'position', 'degree', 'is_active']
    list_filter = ['department', 'degree']
    list_editable = ['is_active']