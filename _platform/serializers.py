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


class AddUpdateMaterialSerializer(ModelSerializer):
    """
    Special serializer, it differs from MaterialSerializer that it does not overwrite for id, and category fields.
    Used for creating and updating material.
    The programmer thinks no need to have two classes (AddMaterialSerializer, UpdateMaterialSerializer)
    """
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
