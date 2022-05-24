from rest_framework.viewsets import ModelViewSet

from _platform.models.Audience.model import Audience
from _platform.models.Audience.serializer import AudienceSerializer, CreateAudienceSerializer


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
