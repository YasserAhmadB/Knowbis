from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

# from Knowbis.serializers_methods import validate_field


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['title']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
