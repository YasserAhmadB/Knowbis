from django.db import models

from material_manager.EnrolledToMaterial.Managers import MaterialManager
from material_manager.Material.model import Material
from users_manager.Audience.model import Audience


class EnrolledToMaterial(models.Model):
    objects = MaterialManager()

    audience = models.ForeignKey(to=Audience, on_delete=models.CASCADE)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)

    class Meta:
        unique_together = [('material', 'audience')]
