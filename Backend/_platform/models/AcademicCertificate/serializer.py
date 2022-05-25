from rest_framework import serializers

from _platform.models.AcademicCertificate.model import AcademicCertificate


class AcademicCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicCertificate
        fields = ['certificate']


class CreateAcademicCertificateSerializer(AcademicCertificateSerializer):
    class Meta(AcademicCertificateSerializer.Meta):
        fields = AcademicCertificateSerializer.Meta.fields.copy()
        fields.extend(['certificate'])
