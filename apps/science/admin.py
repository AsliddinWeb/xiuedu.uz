from django.contrib import admin
from .models import Project, Conference, Journal, Publication


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader', 'status', 'is_active']
    list_filter = ['status']
    list_editable = ['is_active']


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'is_upcoming', 'is_active']
    list_filter = ['is_upcoming']
    list_editable = ['is_upcoming', 'is_active']


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['name', 'issn', 'is_active']
    list_editable = ['is_active']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'journal', 'year']
    list_filter = ['journal', 'year']