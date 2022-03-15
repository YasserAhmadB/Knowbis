from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from _platform.models import Category, Material
from _platform.serializers import CategorySerializer, MaterialSerializer, AddUpdateMaterialSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class MaterialViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Material.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return AddUpdateMaterialSerializer
        return MaterialSerializer
