from rest_framework import serializers

from _platform.models import AudienceRateMaterial


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
