from django.db.models.signals import post_save
from django.dispatch import receiver

from .model import Audience
from authenticator.models import User


@receiver(post_save, sender=User)
def create_audience_profile(sender, instance, created, **kwargs):
    if created:
        audience = Audience.objects.create(user=instance)
        audience.save()
