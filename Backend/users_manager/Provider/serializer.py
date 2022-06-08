from django.conf import settings
from rest_framework import serializers

from users_manager.Provider.model import Provider


class ProviderSerializer(serializers.ModelSerializer):  # Logged in user
    class Meta:
        model = Provider
        fields = ['id', 'pic', 'description', 'major']


class RetrieveProviderSerializer(ProviderSerializer):  # Logged in user
    user = settings.DJOSER['SERIALIZERS']['user']

    class Meta(ProviderSerializer.Meta):
        fields = ProviderSerializer.Meta.fields.copy()
        fields.extend(['user'])


class UpdateProviderSerializer(ProviderSerializer):
    pass


class CreateProviderSerializer(ProviderSerializer):
    def save(self, **kwargs):
        user_id = self.context['user_id']
        provider = Provider.objects.create(user_id=user_id, **self.validated_data)
        provider.save()
        return provider
