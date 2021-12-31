from django.contrib import admin
from .models import Category, CategorizedItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'label'
    ]

    search_fields = [
        'label'
    ]


@admin.register(CategorizedItem)
class CategorizedItemAdmin(admin.ModelAdmin):
    pass
    list_display = [
        'content_object', 'category'
    ]
    #
    # search_fields = [
    #     'label'
    # ]
