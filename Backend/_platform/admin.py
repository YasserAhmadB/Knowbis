from django.contrib import admin

from .models.Category.model import Category
from .models.Provider.model import Provider
from .models.Material.model import Material
from .models.Lecture.model import Lecture
from .models.Audience.model import Audience
from .models.Document.model import Document
# from .models.EnrolledToMaterial.model import EnrolledToMaterial
# from .models.Rate.model import AudienceRateMaterial


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
        'duration',
        'is_blocked',
    )
    list_filter = ('category', 'provider', 'last_update', 'is_blocked')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'material',
        'brief_description',
        'text',
        'video',
        'duration',
    )
    list_filter = ('material',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'lecture')
    list_filter = ('lecture',)


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_filter = ('user',)


# @admin.register(EnrolledToMaterial)
# class EnrolledToMaterialAdmin(admin.ModelAdmin):
#     list_display = ('id', 'audience', 'material')
#     list_filter = ('audience', 'material')


# @admin.register(AudienceRateMaterial)
# class AudienceRateMaterialAdmin(admin.ModelAdmin):
#     list_display = ('id', 'audience', 'material', 'rating')
#     list_filter = ('audience', 'material', 'rating')
