from django.db import models

from _platform.models.Lecture.model import Lecture


class Document(models.Model):
    file = models.FileField()
    lecture = models.ForeignKey(to=Lecture, on_delete=models.CASCADE)
