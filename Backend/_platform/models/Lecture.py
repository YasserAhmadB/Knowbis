from django.db import models
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from _platform.models.Material import Material
from authorizer.permissions import IsLectureProviderOrReadOnly


class Lecture(models.Model):  # Lecture
    title = models.CharField(max_length=255)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    brief_description = models.CharField(max_length=1255)
    text = models.CharField(max_length=2555)
    video = models.URLField()


class AddUpdateLectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['title', 'brief_description', 'text', 'video']


class AddLectureSerializer(AddUpdateLectureSerializer):
    def save(self, **kwargs):
        material_id = self.context['material_id']
        lecture = Lecture.objects.create(material_id=material_id, **self.validated_data)
        lecture.save()
        return lecture


class UpdateLectureSerializer(AddUpdateLectureSerializer):
    pass


class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'brief_description', 'text', 'video']


class LecturesViewSet(ModelViewSet):  # Lectures
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsLectureProviderOrReadOnly]  # Does not work (https://www.django-rest-framework.org/api-guide/permissions/)

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

