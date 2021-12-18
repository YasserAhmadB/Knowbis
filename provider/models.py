from django.conf import settings
from django.contrib import admin
from django.db import models


# Create your models here.
class Provider(models.Model):
    STATUS_ACTIVE = 'A'
    STATUS_BLOCKED = 'B'
    STATUS_VERIFIED = 'V'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_VERIFIED, 'Verified'),
        (STATUS_BLOCKED, 'Blocked'),
    ]

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']


class ProviderDocuments(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    document = models.FileField()

