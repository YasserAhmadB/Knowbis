from django.core.validators import MaxValueValidator
from django.db import models

from _platform.models.Category.model import Category
from _platform.models.Provider.model import Provider


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
    brief_description = models.CharField(max_length=1255, null=True)  # x

    image = models.ImageField(null=True)
    last_update = models.DateField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=PRIVATE_CHOICE)
    requirements = models.CharField(max_length=1255, null=True)
    what_will_learn = models.CharField(max_length=1255)
    duration = models.PositiveIntegerField(validators=[MaxValueValidator(12000)])

    is_blocked = models.BooleanField(default=False)


    # rating will be in the serializer
    # the count of enrolled students will be in the serializer
