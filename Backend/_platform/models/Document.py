from django.db import models

from _platform.models.Lecture import Lecture


class Document(models.Model):
    file = models.FileField()
    content = models.ForeignKey(to=Lecture, on_delete=models.CASCADE)
