print("[APPS] before")
from django.apps import AppConfig
print("[APPS] after")


class TagsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category'
