from django.db import models
from category.models import Category


class Material(models.Model):
    title = models.CharField(
        max_length=255
    )

    description = models.CharField(
        max_length=1255
    )

    image = models.ImageField()

    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True
    )
