"""All apps."""
from django.apps import AppConfig


class MainConfig(AppConfig):
    """Class mainconfig."""

    name = 'main'

    def ready(self):
        """Func for signals."""
        import main.signals  # noqa