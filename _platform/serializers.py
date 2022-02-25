from rest_framework import serializers

from _platform.models import Material


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['title', 'provider', 'description', 'image', 'category']

