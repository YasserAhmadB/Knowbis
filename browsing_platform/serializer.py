print("[Serializer] before")
from rest_framework import serializers
print("[Serializer] After")


class MaterialSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=255
    )

    description = serializers.CharField(
        max_length=1255
    )

    image = serializers.ImageField()

    category = serializers.StringRelatedField()
