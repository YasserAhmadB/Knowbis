from rest_framework import serializers

from users_manager.Audience.model import Audience


class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = ['id', 'user']


class CreateAudienceSerializer(AudienceSerializer):
    def save(self, **kwargs):
        user_id = self.context['user_id']
        audience = Audience.objects.create(user_id=user_id, **self.validated_data)
        audience.save()
        return audience
