from django.db import models
from rest_framework.serializers import ModelSerializer

from Knowbis.serializers_methods import validate_field
from _platform.models.Category import Category, CategorySerializer
from _platform.models.Provider import Provider, ProviderSerializer


class Material(models.Model):  # Course
    PRIVATE_CHOICE = 'Private'
    PUBLIC_CHOICE = 'Public'
    STATUS_CHOICES = [
        ('Pr', PRIVATE_CHOICE),
        ('Pu', PUBLIC_CHOICE),
    ]

    title = models.CharField(max_length=255)

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    description = models.CharField(max_length=1255, null=True)
    brief_description = models.CharField(max_length=1255, null=True)

    image = models.ImageField()
    last_update = models.DateField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=PRIVATE_CHOICE)
    requirements = models.CharField(max_length=1255, null=True)
    what_will_learn = models.CharField(max_length=1255)

    # rating will be in the serializer
    # the count of enrolled students will be in the serializer


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