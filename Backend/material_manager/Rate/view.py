from rest_framework.viewsets import ModelViewSet

from material_manager.Rate.model import AudienceRateMaterial
from material_manager.Rate.serializer import AudienceRateMaterialSerializer
from users_manager.Audience.model import Audience


class AudienceRateMaterialViewSet(ModelViewSet):
    queryset = AudienceRateMaterial.objects.all()
    serializer_class = AudienceRateMaterialSerializer
    http_method_names = ['post', 'get']

    def get_serializer_context(self):
        return {
            'material_id': self.kwargs['material_pk'],
            'audience_id': Audience.objects.get(user_id=self.request.user).id,
        }
