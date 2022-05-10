from django.db import models

from _platform.models.Content import Content


class Document(models.Model):
    file = models.FileField()
    content = models.ForeignKey(to=Content, on_delete=models.CASCADE)
