from rest_framework.viewsets import ModelViewSet

from _platform.models import Provider
from _platform.models.Provider.serializer import CreateProviderSerializer, UpdateProviderSerializer, \
    RetrieveProviderSerializer, ProviderSerializer
from authorizer.permissions import IsAdminOrReadOnly, IsMe


class ProviderViewSet(ModelViewSet):
    permission_classes = [IsMe]
    queryset = Provider.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateProviderSerializer
        elif self.request.method == 'PATCH':
            return UpdateProviderSerializer
        elif self.request.method == 'GET':
            return RetrieveProviderSerializer
        return ProviderSerializer

    def get_serializer_context(self):
        print('self.request.data:', self.request.content_type)
        return {'user_id': self.request.user.id}
