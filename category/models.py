print("[Models] before")
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
print("[Models] After")


# class CategorizedItemManager(models.Manager):
#     def get_categories_for(self, obj_type, obj_id):
#         content_type = ContentType.objects.get_for_model(obj_type)
#
#         return CategorizedItem.objects \
#             .select_related('category') \
#             .filter(
#                 content_type=content_type,
#                 object_id=obj_id
#             )


class Category(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label

    class Meta:
        ordering = ['label']


class CategorizedItem(models.Model):
    # objects = CategorizedItemManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
