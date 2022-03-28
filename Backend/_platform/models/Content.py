from django.db import models
from rest_framework.serializers import ModelSerializer

from _platform.models.Document import Document
from _platform.models.Material import Material


class Content(models.Model):  # Lecture
    title = models.CharField(max_length=255)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    brief_description = models.CharField(max_length=1255)
    content = models.CharField(max_length=2555)
    video = models.FileField()
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE, null=True)
    order = models.PositiveIntegerField()

    # class Meta:
    #     unique_together = (("id", "order"),)


class AddUpdateContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['title', 'material_id', 'brief_description', 'content', 'video', 'document', 'order']


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
        fields = ['id', 'material', 'title', 'brief_description', 'content', 'video', 'document', 'order']


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'material', 'title', 'brief_description', 'content', 'video', 'document', 'order']