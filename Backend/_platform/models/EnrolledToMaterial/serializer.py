from rest_framework import serializers

from _platform.models import EnrolledToMaterial
from _platform.models.Material.serializer import BriefMaterialSerializer


class EnrolledToMaterialSerializer(serializers.ModelSerializer):
    material = BriefMaterialSerializer()

    class Meta:
        model = EnrolledToMaterial
        fields = ['material']
