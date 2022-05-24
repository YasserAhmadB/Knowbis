from django.db import models

from _platform.models.Audience.model import Audience
from _platform.models.Material.model import Material


class EnrolledToMaterial(models.Model):
    audience = models.ForeignKey(to=Audience, on_delete=models.CASCADE)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)

    class Meta:
        unique_together = [('material', 'audience')]
