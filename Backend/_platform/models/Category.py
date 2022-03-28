from django.db import models
from rest_framework.serializers import ModelSerializer

from Knowbis.serializers_methods import validate_field


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class CategorySerializer(ModelSerializer):
    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Category
        fields = ['id', 'title']