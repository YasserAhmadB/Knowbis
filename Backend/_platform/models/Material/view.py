from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authorizer.permissions import IsMaterialProviderOrReadOnly, IsProviderOrReadOnly

from _platform.models.EnrolledToMaterial.model import EnrolledToMaterial
from _platform.models.EnrolledToMaterial.serializer import EnrolledToMaterialSerializer

from _platform.models.Material.model import Material
from _platform.models.Material.serializer import AddUpdateMaterialSerializer, BriefRetrieveMaterialSerializer,\
    RetrieveMaterialSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects\
        .select_related('category')\
        .select_related('provider')\
        .filter(is_blocked=False)

    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsMaterialProviderOrReadOnly, IsProviderOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title']

    @action(detail=False)
    def uploaded(self, request):
        queryset = Material.objects.filter(provider__user_id=request.user.id)
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def enrolled(self, request):

        queryset = EnrolledToMaterial.objects.filter(audience__user_id=request.user.id)
        print('queryset:', queryset)
        serializer = EnrolledToMaterialSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def enroll(self, request, pk):
        from _platform.models.EnrolledToMaterial.model import EnrolledToMaterial
        from _platform.models.Audience.model import Audience

        enrolled_to_material = EnrolledToMaterial()
        enrolled_to_material.material_id = pk
        enrolled_to_material.audience = Audience.objects.get(user_id=request.user.id)

        try:
            enrolled_to_material.save()
        except:
            return Response('You are already enrolled in this course')

        return Response('ok')

    @action(detail=True)
    def drop(self, request, pk):
        try:
            enrolled_to_material = EnrolledToMaterial.objects.get(material_id=pk, audience__user_id=request.user.id)
            enrolled_to_material.delete()
        except:
            return Response('You are not enrolled in the course')

        return Response('ok')

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return AddUpdateMaterialSerializer
        elif self.request.method == 'GET':
            if self.action == 'list':  # if the endpoint is /materials it will return a brief materialssss
                return BriefRetrieveMaterialSerializer
            else:
                return RetrieveMaterialSerializer
        return MaterialViewSet

    def get_serializer_context(self):
        if self.action == 'retrieve':
            return {
                'material_id': self.kwargs['pk'],
            }
        if self.request.method == 'POST':
            return {
                'provider_id': self.queryset.filter()
            }
