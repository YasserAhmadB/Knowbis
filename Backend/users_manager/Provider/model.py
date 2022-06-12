from django.conf import settings
from django.db import models


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    major = models.CharField(max_length=255)
    pic = models.ImageField(null=True)
    description = models.CharField(max_length=1255, null=True, blank=True)
    # certificate = models.FileField(null=True)
