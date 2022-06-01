from django.apps import AppConfig


class PlatformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '_platform'

    def ready(self):
        import _platform.models.Audience.signals
