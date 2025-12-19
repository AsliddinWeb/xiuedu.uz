from django.contrib import admin
from .models import Admission, Fee, Application, ExamSchedule


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'is_active']
    list_filter = ['level']
    list_editable = ['is_active']


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ['program', 'form', 'amount', 'year', 'is_active']
    list_filter = ['form', 'year']
    list_editable = ['is_active']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'program', 'status', 'created_at']
    list_filter = ['status', 'program']
    list_editable = ['status']
    readonly_fields = ['created_at']


@admin.register(ExamSchedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'is_active']
    list_editable = ['is_active']