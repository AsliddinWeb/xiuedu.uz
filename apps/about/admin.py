from django.contrib import admin
from .models import About, Rector, Staff, Document


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Rector)
class RectorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'phone']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'created_at']
    list_filter = ['category']
    list_editable = ['order']