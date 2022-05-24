from django.db import models
from _platform.models.Material.model import Material


class Lecture(models.Model):  # Lecture
    title = models.CharField(max_length=255)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    brief_description = models.CharField(max_length=1255)
    text = models.CharField(max_length=2555)
    video = models.URLField()
    duration = models.CharField(max_length=10)
