from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from .adapter import Category
from .adapter import CategorizedItem


class MaterialManager(models.Manager):
    def get_categories_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        return CategorizedItem.objects \
            .select_related('category') \
            .filter(
            content_type=content_type,
            object_id=obj_type
        )


class Material(models.Model):
    objects = MaterialManager()
    title = models.CharField(
        max_length=255
    )

    description = models.CharField(
        max_length=1255
    )

    image = models.ImageField()

    # category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    category = GenericRelation(CategorizedItem, content_type_field='content_type_fk', object_id_field='object_primary_key', null=True)

    def __str__(self):
        return f"{self.title}"
