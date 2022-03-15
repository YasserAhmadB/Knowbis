from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Material(models.Model):
    title = models.CharField(max_length=255)

    # provider = models.ForeignKey(Provider, on_delete=models.CASCADE)  # Later

    description = models.CharField(max_length=1255, null=True)

    # image = models.ImageField()  # Part 3
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
