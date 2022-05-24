from django.db import models

from _platform.models import Audience, Material


class AudienceRateMaterial(models.Model):
    audience = models.ForeignKey(to=Audience, on_delete=models.CASCADE)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    rating = models.BooleanField()
