from rest_framework.viewsets import ModelViewSet

from _platform.models import Provider
from _platform.models.Provider.serializer import CreateProviderSerializer, UpdateProviderSerializer, ProviderSerializer


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
