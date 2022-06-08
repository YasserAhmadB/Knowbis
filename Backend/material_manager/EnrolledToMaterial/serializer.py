from rest_framework import serializers

from material_manager.EnrolledToMaterial.model import EnrolledToMaterial
from material_manager.Material.serializer import BriefRetrieveMaterialSerializer


class EnrolledToMaterialSerializer(serializers.ModelSerializer):
    material = BriefRetrieveMaterialSerializer()

    class Meta:
        model = EnrolledToMaterial
        fields = ['material']
