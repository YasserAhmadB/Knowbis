from django.db import models
from django.conf import settings


class Document(models.Model):
    file = models.FileField()


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


class Material(models.Model):  # Course
    PRIVATE_CHOICE = 'Private'
    PUBLIC_CHOICE = 'Public'
    STATUS_CHOICES = [
        ('Pr', PRIVATE_CHOICE),
        ('Pu', PUBLIC_CHOICE),
    ]

    title = models.CharField(max_length=255)

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    description = models.CharField(max_length=1255, null=True)
    brief_description = models.CharField(max_length=1255, null=True)

    image = models.ImageField()
    last_update = models.DateField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=PRIVATE_CHOICE)
    requirements = models.CharField(max_length=1255, null=True)
    what_will_learn = models.CharField(max_length=1255)

    # rating will be in the serializer
    # the count of enrolled students will be in the serializer


class Content(models.Model):  # Lecture
    title = models.CharField(max_length=255)
    material = models.ForeignKey(to=Material, on_delete=models.CASCADE)
    brief_description = models.CharField(max_length=1255)
    content = models.CharField(max_length=2555)
    video = models.FileField()
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE, null=True)
    order = models.PositiveIntegerField()

    # class Meta:
    #     unique_together = (("id", "order"),)
