print("[ADMIN] before")
from django.contrib import admin
from .models import Category
from .models import CategorizedItem
print("[ADMIN] after")


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'label']
    search_fields = ['label']


admin.site.register(CategorizedItem)
