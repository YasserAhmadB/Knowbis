from django.db import models
from django.conf import settings
from rest_framework import mixins
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pic = models.ImageField(null=True)
    description = models.CharField(max_length=1255, null=True)


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


class ProviderViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateProviderSerializer
        elif self.request.method == 'PATCH':
            return UpdateProviderSerializer
        return ProviderSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
