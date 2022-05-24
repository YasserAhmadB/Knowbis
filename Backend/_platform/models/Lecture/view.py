from rest_framework.viewsets import ModelViewSet

from _platform.models import Lecture
from _platform.models.Lecture.serializer import AddLectureSerializer, UpdateLectureSerializer, LectureSerializer
from authorizer.permissions import IsLectureProviderOrReadOnly


class LecturesViewSet(ModelViewSet):  # Lectures
    http_method_names = ['get', 'post', 'patch', 'delete']

    # Does not work (https://www.django-rest-framework.org/api-guide/permissions/)
    permission_classes = [IsLectureProviderOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddLectureSerializer
        elif self.request.method == 'PATCH':
            return UpdateLectureSerializer
        return LectureSerializer

    def get_queryset(self):
        queryset = Lecture.objects.filter(material_id=self.kwargs['material_pk'])
        return queryset

    def get_serializer_context(self):
        return {'material_id': self.kwargs['material_pk']}
