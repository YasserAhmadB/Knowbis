from rest_framework.viewsets import ModelViewSet

from _platform.models.Category.model import Category
from _platform.models.Category.serializer import CategorySerializer
from authorizer.permissions import IsAdminOrReadOnly


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']
