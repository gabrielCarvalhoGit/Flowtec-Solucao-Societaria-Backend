from django.apps import AppConfig


class SocietarioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.societario"

    def ready(self):
        import apps.societario.infra.models 