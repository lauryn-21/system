from django.apps import AppConfig


class HighAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'high_app'

    def ready(self):
        import high_app.signals