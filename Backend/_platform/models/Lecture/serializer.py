from rest_framework.serializers import ModelSerializer

from _platform.models import Lecture


class AddUpdateLectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['title', 'brief_description', 'text', 'video', 'duration']


class AddLectureSerializer(AddUpdateLectureSerializer):
    def save(self, **kwargs):
        material_id = self.context['material_id']
        print('material_id:', material_id)
        lecture = Lecture.objects.create(material_id=material_id, **self.validated_data)
        lecture.save()
        return lecture


class UpdateLectureSerializer(AddUpdateLectureSerializer):
    pass


class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'brief_description', 'text', 'video', 'duration']


class BriefRetrieveLectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'duration', 'brief_description']
