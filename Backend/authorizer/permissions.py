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


class IsProviderOrReadOnly(permissions.BasePermission):
    from _platform.models.Provider.model import Provider

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            self.Provider.objects.get(user_id=request.user.id)
            return True
        except:
            return False





class IsLectureProviderOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.material.provider.user == request.user)

