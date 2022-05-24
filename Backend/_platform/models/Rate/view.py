from rest_framework.viewsets import ModelViewSet

from _platform.models import AudienceRateMaterial, Audience
from _platform.models.Rate.serializer import AudienceRateMaterialSerializer


class AudienceRateMaterialViewSet(ModelViewSet):
    queryset = AudienceRateMaterial.objects.all()
    serializer_class = AudienceRateMaterialSerializer
    http_method_names = ['post', 'get']


    def get_serializer_context(self):
        return {
            'material_id': self.kwargs['material_pk'],
            'audience_id': Audience.objects.get(user_id=self.request.user).id,
        }
