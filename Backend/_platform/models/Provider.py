from django.db import models
from django.conf import settings
from rest_framework import mixins
from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet

from _platform.models import Document


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pic = models.ImageField()
    description = models.CharField(max_length=1255)
    # documents = models.ManyToOneRel(to=Document, field_name='documents', on_delete=models.SET_NULL, )

    def __str__(self):
        return f'{self.user.first_name}'

    class Meta:
        ordering = ['user__first_name']
        # permissions = [
        # ('block_provider', 'Can block a provider'),
        # ('unblock_provider', 'Can unblock a provider'),
        # ('verify_provider', 'Can verify a provider'),
        # ]


class ProviderSerializer(serializers.ModelSerializer):

    user = settings.DJOSER['SERIALIZERS']['user']

    class Meta:
        model = Provider
        fields = ['id', 'user', 'pic', 'description']


class UpdateProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['pic', 'description']


class ProviderViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateProviderSerializer
        return ProviderSerializer
