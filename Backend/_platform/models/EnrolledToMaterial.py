from django.db import models

from _platform.models.Audience import Audience
from _platform.models.Material import Material, BriefMaterialSerializer
from rest_framework import serializers


class EnrolledToMaterial(models.Model):
    audience = models.ForeignKey(to=Audience, on_delete=models.CASCADE)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)

    class Meta:
        unique_together = [('material', 'audience')]


class EnrolledToMaterialSerializer(serializers.ModelSerializer):
    material = BriefMaterialSerializer()

    class Meta:
        model = EnrolledToMaterial
        fields = ['material']
