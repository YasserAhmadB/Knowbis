from django.contrib import admin


# Register your models here.
from .models import Provider, ProviderDocuments


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'status']
    list_editable = ['status']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


@admin.register(ProviderDocuments)
class ProviderDocumentsAdmin(admin.ModelAdmin):
    list_display = ['document']
    # list_editable = ['status']
    list_per_page = 10
    # list_select_related = ['user']
    # ordering = ['user__first_name', 'user__last_name']
    # search_fields = ['first_name__istartswith', 'last_name__istartswith']
