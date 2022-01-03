from django.contrib.contenttypes.models import ContentType
from django.db import models

from Knowbis.settings import AUTH_USER_MODEL
from .adapter import Category


class MaterialManager(models.Manager):
    def get_categories_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        return Material.objects \
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

    # instructor = models.CharField(
    #     max_length=255,
    #     default=AUTH_USER_MODEL
    # )
    instructor = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    likes = models.IntegerField(default=0)

    description = models.CharField(
        max_length=1255,
        null=True
    )

    image = models.ImageField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
