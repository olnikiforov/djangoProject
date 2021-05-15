"""All apps."""
from django.apps import AppConfig


class MainConfig(AppConfig):
    """Class mainconfig."""

    default_auto_field = 'django.db.models.AutoField'
    name = 'main'

    def ready(self):
        """Func for signals."""
        import main.signals  # noqa