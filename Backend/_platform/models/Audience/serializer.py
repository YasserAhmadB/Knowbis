from rest_framework import serializers

from _platform.models.Audience.model import Audience


class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = ['id', 'user']


class CreateAudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = ['id', 'user']

    def save(self, **kwargs):
        user_id = self.context['user_id']
        provider = Audience.objects.create(user_id=user_id, **self.validated_data)
        provider.save()
        return provider
