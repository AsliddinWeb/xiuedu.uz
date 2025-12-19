from django.contrib import admin
from .models import Partner, Grant, Exchange, Agreement


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'order', 'is_active']
    list_filter = ['country']
    list_editable = ['order', 'is_active']


@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'deadline', 'is_active']
    list_editable = ['is_active']


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'duration', 'deadline', 'is_active']
    list_filter = ['country']
    list_editable = ['is_active']


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ['title', 'partner', 'signed_date']
    list_filter = ['partner']