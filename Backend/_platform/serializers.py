from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Knowbis.serializers_methods import validate_field
from .models import Category, Material, Provider, Content


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
        fields = ['title', 'category', 'provider', 'description', 'brief_description', 'image', 'last_update',
                  'requirements', 'what_will_learn', 'status']


class DeleteMaterialSerializer(ModelSerializer):
    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['id']


class BriefMaterialSerializer(ModelSerializer):
    category = CategorySerializer()
    provider = ProviderSerializer()

    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['id', 'title', 'category', 'provider', 'brief_description', 'image', 'last_update', 'status'
                  # , 'rating', 'enrolled_students'
                  ]


class MaterialSerializer(ModelSerializer):
    category = CategorySerializer()
    provider = ProviderSerializer()

    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['title', 'category', 'provider', 'description', 'image', 'last_update', 'status', 'requirements',
                  'what_will_learn'
                  # , 'rating', 'enrolled_students'
                  ]


class AddUpdateContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'material_id', 'brief_description', 'content', 'video', 'document', 'order']


class AddContentSerializer(AddUpdateContentSerializer):
    def save(self, **kwargs):
        material_id = self.context['material_id']
        print("material_id:", material_id)
        self.instance = Content.objects.create(material_id=material_id, **self.validated_data)
        return self.instance


class UpdateContentSerializer(AddUpdateContentSerializer):
    pass


class DeleteContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id']


class BriefContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'material', 'title', 'brief_description', 'content', 'video', 'document', 'order']


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'material', 'title', 'brief_description', 'content', 'video', 'document', 'order']
