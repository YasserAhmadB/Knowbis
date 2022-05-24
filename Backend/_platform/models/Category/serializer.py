from rest_framework.serializers import ModelSerializer

from _platform.models.Category.model import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
