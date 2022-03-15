from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Knowbis.serializers_methods import validate_field
from .models import Category, Material


class CategorySerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Category
        fields = ['id', 'title']


class SimpleCategorySerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id']


class AddMaterialSerializer(ModelSerializer):
    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['title', 'description', 'category']


class UpdateMaterialSerializer(ModelSerializer):
    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['title', 'description', 'category']


class MaterialSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = CategorySerializer()

    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['id', 'title', 'description', 'category']
