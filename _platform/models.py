from django.db import models
from django.conf import settings


class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    major = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.first_name} {self.major}'

    class Meta:
        ordering = ['user__first_name', 'major']
        permissions = [
            ('block_provider', 'Can block a provider'),
            ('unblock_provider', 'Can unblock a provider'),
            ('verify_provider', 'Can verify a provider'),
        ]


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Material(models.Model):
    title = models.CharField(max_length=255)

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    description = models.CharField(max_length=1255, null=True)

    # image = models.ImageField()  # Part 3
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
