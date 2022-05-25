from django.conf import settings
from django.db import models


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pic = models.ImageField(null=True)
    description = models.CharField(max_length=1255, null=True)
    major = models.CharField(max_length=255)
