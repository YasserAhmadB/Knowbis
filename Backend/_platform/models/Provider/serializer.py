from django.conf import settings
from rest_framework import serializers

from _platform.models import Provider


class ProviderSerializer(serializers.ModelSerializer):  # Logged in user
    user = settings.DJOSER['SERIALIZERS']['user']

    class Meta:
        model = Provider
        fields = ['id', 'user', 'pic', 'description']


class UpdateProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['pic', 'description']


class CreateProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['pic', 'description']

    def save(self, **kwargs):
        user_id = self.context['user_id']
        provider = Provider.objects.create(user_id=user_id, **self.validated_data)
        provider.save()
        return provider
