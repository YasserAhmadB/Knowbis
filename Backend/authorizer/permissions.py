from rest_framework import permissions

from users_manager.Provider.model import Provider


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsMe(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsMaterialProviderOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.provider.user == request.user


class IsProviderOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            Provider.objects.get(user_id=request.user.id)
            return True
        except:
            return False


class IsLectureProviderOrReadOnly(permissions.BasePermission):
    def __init__(self, provider__user_id):
        self.provider__user_id = provider__user_id

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.material.provider__user_id.user == request.user)

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return self.provider__user_id == request.user.id
