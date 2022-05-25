from rest_framework.serializers import ModelSerializer

from _platform.models import Lecture


class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'brief_description', 'text', 'video', 'duration']


class AddLectureSerializer(LectureSerializer):
    def save(self, **kwargs):
        material_id = self.context['material_id']
        print('material_id:', material_id)
        lecture = Lecture.objects.create(material_id=material_id, **self.validated_data)
        lecture.save()
        return lecture


class UpdateLectureSerializer(LectureSerializer):
    pass


class BriefRetrieveLectureSerializer(LectureSerializer):
    class Meta(LectureSerializer.Meta):
        fields = ['id', 'title', 'brief_description', 'duration']
