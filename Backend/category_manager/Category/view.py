from rest_framework.viewsets import ModelViewSet

from category_manager.Category.model import Category
from category_manager.Category.serializer import CategorySerializer
from authorizer.permissions import IsAdminOrReadOnly


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']
