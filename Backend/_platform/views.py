# Create your views here.
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from .models import Category, Material, Provider
from .serializers import CategorySerializer, MaterialSerializer, AddUpdateMaterialSerializer, \
    ProviderSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return AddUpdateMaterialSerializer
        return MaterialSerializer


class ProviderViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    # def get_serializer_class(self):
    #     if self.request.method == 'POST' or self.request.method == 'PATCH':
    #         return AddUpdateMaterialSerializer
    #     return MaterialSerializer
