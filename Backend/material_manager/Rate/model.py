from django.db import models

from material_manager.Material.model import Material
from users_manager.Audience.model import Audience


class AudienceRateMaterial(models.Model):
    audience = models.ForeignKey(to=Audience, on_delete=models.CASCADE)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    rating = models.BooleanField()
