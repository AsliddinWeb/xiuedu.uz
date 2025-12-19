from django.contrib import admin
from .models import Contact, FAQ, Vacancy, Appeal


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read']
    list_editable = ['is_read']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'deadline', 'is_active', 'created_at']
    list_editable = ['is_active']


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'subject', 'status', 'created_at']
    list_filter = ['status']
    list_editable = ['status']