from django.db import models
from django.conf import settings
from rest_framework.serializers import ModelSerializer


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    major = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.first_name} {self.major}'

    class Meta:
        ordering = ['user__first_name', 'major']
        permissions = [
            ('block_provider', 'Can block a provider'),
            ('unblock_provider', 'Can unblock a provider'),
            ('verify_provider', 'Can verify a provider'),
        ]


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ['major', 'user']