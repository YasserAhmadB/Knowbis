from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authorizer.permissions import IsMaterialProviderOrReadOnly, IsProviderOrReadOnly

from material_manager.EnrolledToMaterial.model import EnrolledToMaterial
from material_manager.EnrolledToMaterial.serializer import EnrolledToMaterialSerializer

from material_manager.Material.model import Material
from material_manager.Material.serializer import AddUpdateMaterialSerializer, BriefRetrieveMaterialSerializer,\
    RetrieveMaterialSerializer
from users_manager.Audience.model import Audience


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
        serializer = EnrolledToMaterialSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def enroll(self, request, pk):
        response = EnrolledToMaterial.objects.enroll(material_id=pk, user_id=request.user.id)
        return Response(response)

    @action(detail=True)
    def drop(self, request, pk):
        response = EnrolledToMaterial.objects.drop(material_id=pk, user_id=request.user.id)
        return Response(response)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return AddUpdateMaterialSerializer
        elif self.request.method == 'GET':
            if self.action == 'list':  # if the endpoint is /materials it will return a brief materials
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
