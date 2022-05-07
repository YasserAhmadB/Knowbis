from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# from Knowbis.serializers_methods import validate_field
from authorizer.permissions import IsAdminOrReadOnly


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']
