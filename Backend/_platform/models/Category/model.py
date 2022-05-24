from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
