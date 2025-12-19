from django.contrib import admin
from .models import Program, Subject, Schedule, Curriculum


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'level', 'form', 'is_active']
    list_filter = ['level', 'form', 'faculty']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'program', 'credits', 'semester']
    list_filter = ['program', 'semester']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'faculty', 'updated_at']
    list_filter = ['faculty']


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ['program', 'year']
    list_filter = ['program']