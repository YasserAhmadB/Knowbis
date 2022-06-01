from rest_framework import serializers

from _platform.models.EnrolledToMaterial.model import EnrolledToMaterial
from _platform.models.Material.serializer import BriefRetrieveMaterialSerializer


class EnrolledToMaterialSerializer(serializers.ModelSerializer):
    material = BriefRetrieveMaterialSerializer()

    class Meta:
        model = EnrolledToMaterial
        fields = ['material']
