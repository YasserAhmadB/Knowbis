from django.db import models
from django.conf import settings
from rest_framework import mixins
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pic = models.ImageField(null=True)
    description = models.CharField(max_length=1255, null=True)

    def __str__(self):
        return f'{self.user.first_name}'

    class Meta:
        ordering = ['user__first_name']
        permissions = [
            ('block_provider', 'Can block a provider'),
            ('unblock_provider', 'Can unblock a provider'),
            ('verify_provider', 'Can verify a provider'),
        ]


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
    user_id = serializers.SerializerMethodField()

    def create(self, validated_data):
        print('self.context["user_id"]:', self.context['user_id'])
        validated_data['user_id'] = self.context['user_id']
        provider = Provider(**validated_data)
        provider.save()
        return provider

    class Meta:
        model = Provider
        fields = ['id', 'user_id', 'pic', 'description']


class ProviderViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ProviderSerializer
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
