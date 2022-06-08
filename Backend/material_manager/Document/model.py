from django.db import models

from material_manager.Lecture.model import Lecture


class Document(models.Model):
    file = models.FileField()
    lecture = models.ForeignKey(to=Lecture, on_delete=models.CASCADE)
