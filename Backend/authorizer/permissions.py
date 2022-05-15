from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsMaterialProviderOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.provider.user == request.user


class IsContentProviderOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # print('obj.material.provider.user == request.user:', obj.material.provider.user == request.user)
        # return obj.material.provider.user == request.user

