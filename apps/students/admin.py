from django.contrib import admin
from .models import Scholarship, Dormitory, StudentLife, StudentResource


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'is_active']
    list_editable = ['is_active']


@admin.register(Dormitory)
class DormitoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'capacity', 'is_active']
    list_editable = ['is_active']


@admin.register(StudentLife)
class StudentLifeAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_active', 'created_at']
    list_editable = ['is_active']


@admin.register(StudentResource)
class StudentResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_filter = ['category']
    list_editable = ['order']