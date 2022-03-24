# Create your views here.
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from .models import Category, Material, Provider, Content
from .serializers import CategorySerializer, MaterialSerializer, AddUpdateMaterialSerializer, \
    ProviderSerializer, DeleteMaterialSerializer, BriefMaterialSerializer, AddContentSerializer, UpdateContentSerializer, \
    DeleteContentSerializer, ContentSerializer, BriefContentSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return AddUpdateMaterialSerializer
        elif self.request.method == 'DELETE':
            return DeleteMaterialSerializer
        if self.action == 'list':  # if the endpoint is /materials it will return a brief material
            return BriefMaterialSerializer
        return MaterialSerializer


class ProviderViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']


class ContentViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddContentSerializer
        elif self.request.method == 'PATCH':
            return UpdateContentSerializer
        elif self.request.method == 'DELETE':
            return DeleteContentSerializer
        if self.action == 'list':  # if the endpoint is /materials it will return a brief material
            return BriefContentSerializer
        return ContentSerializer

    def get_queryset(self):
        queryset = Content.objects.filter(material_id=self.kwargs['material_pk'])
        return queryset

    def get_serializer_context(self):
        return {'material_id': self.kwargs['material_pk']}