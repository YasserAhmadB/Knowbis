from django.conf import settings
from rest_framework import serializers

from _platform.models import Provider


class ProviderSerializer(serializers.ModelSerializer):  # Logged in user
    class Meta:
        model = Provider
        fields = ['id', 'pic', 'description']


class RetrieveProviderSerializer(ProviderSerializer):  # Logged in user
    user = settings.DJOSER['SERIALIZERS']['user']
    # pass
    class Meta(ProviderSerializer.Meta):
        ProviderSerializer.Meta.fields.extend(['user'])


class UpdateProviderSerializer(ProviderSerializer):
    pass


class CreateProviderSerializer(ProviderSerializer):
    def save(self, **kwargs):
        user_id = self.context['user_id']
        provider = Provider.objects.create(user_id=user_id, **self.validated_data)
        provider.save()
        return provider
