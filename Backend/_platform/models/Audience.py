from django.db import models
from django.conf import settings
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet


class Audience(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


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


class AudienceViewSet(ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    http_method_names = ['get', 'post']

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAudienceSerializer
        return AudienceSerializer

