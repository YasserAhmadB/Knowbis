from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers

from users_manager.Provider.model import Provider


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class UserRetrieveSerializer(BaseUserSerializer):
    is_instructor = serializers.SerializerMethodField()

    def get_is_instructor(self, user):
        if Provider.objects.filter(user_id=user.id).count() > 0:
            return True
        return False

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_instructor']
