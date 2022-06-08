from rest_framework.serializers import ModelSerializer

from category_manager.Category.model import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
