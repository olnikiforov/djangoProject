"""Notify."""
from django.core.mail import send_mail


def notify(email_to):
    """Notify Method."""
    email_send(email_to)


def email_send(email_to):
    """Notify Email."""
    send_mail(
        'Some Topic',
        'It is just Notifying!',
        'nikiforovsh@knu.ua',
        [email_to],
        fail_silently=False
    )


def telegram_notify(email_to):
    """Notify Telegram."""
    pass
