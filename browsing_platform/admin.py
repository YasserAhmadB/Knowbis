from django.contrib import admin

from category.models import Category, CategorizedItem
from .models import Material


# Register your models here.


# @admin.register(Material)
# class MaterialAdmin(admin.ModelAdmin):
#     pass
#     list_display = [
#         'title',
#         # 'category'
#     ]
#
#     search_fields = [
#         'label',
#         # 'category'
#     ]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    # inlines = [CategorizedItemInLine]
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('title', 'category'),
    #     }),
    # )
    list_display = [
        'title', 'category'
    ]
