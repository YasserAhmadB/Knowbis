from django.contrib import admin

from .models.Category.model import Category
from .models.Provider.model import Provider
from .models.Material.model import Material
from .models.Lecture.model import Lecture
from .models.Document.model import Document
from .models.Audience.model import Audience
from .models.EnrolledToMaterial.model import EnrolledToMaterial


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


@admin.register(Lecture)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'material',
        'brief_description',
        'text',
        'video',
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
