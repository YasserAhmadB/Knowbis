from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Knowbis.serializers_methods import validate_field
from _platform.models.Rate.model import AudienceRateMaterial
from _platform.models.Material.model import Material
from _platform.models.Category.serializer import CategorySerializer
from _platform.models.Provider.serializer import ProviderSerializer


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
                  'requirements', 'what_will_learn', 'status', 'duration']


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

    enrolled_students = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    def get_rating(self, material):
        print(1)
        ratings = AudienceRateMaterial.objects.filter(material_id=material.id)
        print(2)
        like = ratings.filter(rating=True).count()
        print(3)
        dislike = ratings.filter(rating=False).count()
        print(4)
        total_ratings = like + dislike
        print(5)
        if total_ratings:
            return like / (like + dislike) * 100
        return 0.0

    def get_enrolled_students(self, material: Material):
        from _platform.models import EnrolledToMaterial
        return EnrolledToMaterial.objects.filter(material=material).count()

    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['id', 'title', 'category', 'provider', 'brief_description', 'image', 'last_update', 'status',
                  'duration', 'enrolled_students', 'rating']


class RetrieveMaterialSerializer(ModelSerializer):
    category = CategorySerializer()
    provider = ProviderSerializer()
    enrolled_students = serializers.SerializerMethodField()

    rating = serializers.SerializerMethodField()

    def get_rating(self, material):
        print(1)
        ratings = AudienceRateMaterial.objects.filter(material_id=material.id)
        print(2)
        like = ratings.filter(rating=True).count()
        print(3)
        dislike = ratings.filter(rating=False).count()
        print(4)
        total_ratings = like + dislike
        print(5)
        if total_ratings:
            return like / (like + dislike) * 100
        return 0.0

    def get_enrolled_students(self, material: Material):
        from _platform.models import EnrolledToMaterial
        return EnrolledToMaterial.objects.filter(material=material).count()

    def validate_title(self, value: str):
        validate_field(value)
        return value

    class Meta:
        model = Material
        fields = ['id', 'title', 'category', 'provider', 'description', 'image', 'last_update', 'status',
                  'requirements', 'what_will_learn', 'duration', 'enrolled_students', 'rating'
                  ]
