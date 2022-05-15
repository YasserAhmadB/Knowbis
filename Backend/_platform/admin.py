from django.contrib import admin

from .models.Category import Category
from .models.Provider import Provider
from .models.Material import Material
from .models.Content import Content
from .models.Document import Document
from .models.Audience import Audience
from .models.EnrolledToMaterial import EnrolledToMaterial


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pic', 'description')
    list_filter = ('user',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'provider',
        'description',
        'brief_description',
        'image',
        'last_update',
        'status',
        'requirements',
        'what_will_learn',
    )
    list_filter = ('category', 'provider', 'last_update')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'material',
        'brief_description',
        'text',
        'video',
        'order',
    )
    list_filter = ('material',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'content')
    list_filter = ('content',)


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_filter = ('user',)


@admin.register(EnrolledToMaterial)
class EnrolledToMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'audience', 'material')
    list_filter = ('audience', 'material')
