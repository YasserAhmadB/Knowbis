from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Category


class CategorySerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    def validate_title(self, value: str):
        if value[0].isdigit():
            raise serializers.ValidationError("Category cannot starts with a number")
        return value

    class Meta:
        model = Category
        fields = ['id', 'title']
