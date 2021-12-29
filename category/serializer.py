print("[Serializer] before")
from rest_framework import serializers
print("[Serializer] After")


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField(max_length=255)


class CategorizedItemSerializer(serializers.Serializer):
    # objects = CategorizedItemManager()
    # category = serializers.ForeignKey(Category, on_delete=models.CASCADE)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = serializers.IntegerField()
    # content_object = serializers.GenericForeignKey()
