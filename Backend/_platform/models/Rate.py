from django.db import models
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from _platform.models import Audience, Material


class AudienceRateMaterial(models.Model):
    audience = models.ForeignKey(to=Audience, on_delete=models.CASCADE)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    rating = models.BooleanField()


class AudienceRateMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudienceRateMaterial
        fields = ['rating']

    def save(self, **kwargs):
        material_id = self.context['material_id']
        audience_id = self.context['audience_id']

        try:
            rate = AudienceRateMaterial.objects.get(material_id=material_id, audience_id=audience_id)
            rate.rating = self.validated_data['rating']
        except:
            rate = AudienceRateMaterial.objects.create(material_id=material_id, audience_id=audience_id, **self.validated_data)
        rate.save()
        return rate


class AudienceRateMaterialViewSet(ModelViewSet):
    queryset = AudienceRateMaterial.objects.all()
    serializer_class = AudienceRateMaterialSerializer
    http_method_names = ['post']

    def get_serializer_context(self):
        return {
            'material_id': self.kwargs['material_pk'],
            'audience_id': Audience.objects.get(user_id=self.request.user).id,
        }
