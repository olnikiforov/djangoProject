"""Middleware file helps to take logs."""
from time import time

from main.models import Logger


class SimpleMiddleware:
    """Middleware class."""

    def __init__(self, get_response):
        """Init func."""
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """Call func."""
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response


def get_client_ip(request):
    """Cet client IP."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class LogMiddleware:
    """Log Middleware class."""

    def __init__(self, get_response):
        """Init func."""
        self.get_response = get_response

    def __call__(self, request):
        """Make a logging."""
        logger = Logger()
        logger.save()
        response = self.get_response(request)
        if request.method == "GET":
            st = time()
            path = request.get_full_path()
            user_ip = get_client_ip(request)
            utm = request.GET.get("utm")
            time_ex = time() - st
            logger = Logger(utm=str(utm), time_execution=time_ex, user_ip=user_ip, path=path)
            logger.save()

        return response
