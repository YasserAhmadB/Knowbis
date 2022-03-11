from django.db import models

from Knowbis.settings import AUTH_USER_MODEL


class Provider(models.Model):
    pass


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Material(models.Model):
    title = models.CharField(max_length=255)

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    description = models.CharField(
        max_length=1255,
        null=True
    )

    image = models.ImageField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Audience(models.Model):
    pass


# class EnrolledMaterial(models.Model):
#     audience = models.ForeignKey(Audience, on_delete=models.CASCADE, primary_key=True)
#     material = models.ForeignKey(Material, on_delete=models.CASCADE, primary_key=True)
