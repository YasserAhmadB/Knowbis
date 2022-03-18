from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Knowbis.serializers_methods import validate_field
from .models import Category, Material, Provider


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ['major', 'user']


class CategorySerializer(ModelSerializer):
    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Category
        fields = ['id', 'title']


class AddUpdateMaterialSerializer(ModelSerializer):
    """
    Special serializer, it differs from MaterialSerializer that it does not overwrite the id, and category fields.
    Used for creating and updating material.
    The programmer thinks that there is no need to have two classes (AddMaterialSerializer, UpdateMaterialSerializer)
    """

    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['title', 'description', 'category', 'provider']


class MaterialSerializer(ModelSerializer):
    category = CategorySerializer()
    provider = ProviderSerializer()

    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['id', 'title', 'description', 'category', 'provider']
