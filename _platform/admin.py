from django.contrib import admin

# Register your models here.
from _platform.models import Provider, Category, Material, Audience

admin.site.register(Provider)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Audience)
