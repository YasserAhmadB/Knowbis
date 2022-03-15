from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from _platform.models import Category
from _platform.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
