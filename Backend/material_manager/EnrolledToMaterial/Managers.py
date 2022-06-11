# This file contains business logic for the material component
from django.db import models

from users_manager.Audience.model import Audience


class MaterialManager(models.Manager):
    def enroll(self, material_id, user_id) -> str:
        from material_manager.EnrolledToMaterial.model import EnrolledToMaterial
        enrolled_to_material = EnrolledToMaterial()
        enrolled_to_material.material_id = material_id
        enrolled_to_material.audience = Audience.objects.get(user_id=user_id)

        try:
            enrolled_to_material.save()
        except:
            return 'You are already enrolled in this course'

        return 'ok'

    def drop(self, material_id, user_id) -> str:
        from material_manager.EnrolledToMaterial.model import EnrolledToMaterial
        try:
            enrolled_to_material = EnrolledToMaterial.objects.get(material_id=material_id, audience__user_id=user_id)
            enrolled_to_material.delete()
        except:
            return'You are not enrolled in the course'

        return'ok'
