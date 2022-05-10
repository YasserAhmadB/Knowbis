from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from _platform.models.Material import Material
from authorizer.permissions import IsContentProviderOrReadOnly


class Content(models.Model):  # Lecture
    title = models.CharField(max_length=255)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    brief_description = models.CharField(max_length=1255)
    text = models.CharField(max_length=2555)
    video = models.FileField()
    order = models.PositiveIntegerField()


class AddUpdateContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'material_id', 'brief_description', 'text', 'video', 'document', 'order']


class AddContentSerializer(AddUpdateContentSerializer):
    def save(self, **kwargs):
        material_id = self.context['material_id']
        print("material_id:", material_id)
        self.instance = Content.objects.create(material_id=material_id, **self.validated_data)
        return self.instance


class UpdateContentSerializer(AddUpdateContentSerializer):
    pass


class DeleteContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id']


class BriefContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'material', 'title', 'brief_description', 'text', 'video', 'document', 'order']


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'material', 'title', 'brief_description', 'text', 'video', 'document', 'order']


class ContentViewSet(ModelViewSet):  # Lectures
    permission_classes = [IsContentProviderOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddContentSerializer
        elif self.request.method == 'PATCH':
            return UpdateContentSerializer
        elif self.request.method == 'DELETE':
            return DeleteContentSerializer
        if self.action == 'list':  # if the endpoint is /materials it will return a brief material
            return BriefContentSerializer
        return ContentSerializer

    def get_queryset(self):
        queryset = Content.objects.filter(material_id=self.kwargs['material_pk'])
        return queryset

    def get_serializer_context(self):
        return {'material_id': self.kwargs['material_pk']}
