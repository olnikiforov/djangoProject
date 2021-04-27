"""Celery tasks."""
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now
from main.models import Logger, Subscriber
from main.notify_service import email_send


@shared_task
def delete_logs():
    """Delete Logs."""
    Logger.objects.filter(created=now() - timedelta(days=3)).delete()


@shared_task
def notify_on_subscription(email_to):
    """Notify on subscription."""
    email_send(email_to)


@shared_task
def notify_subs():
    """Delete Logs."""
    subs = Subscriber.objects.values_list('email_to', flat=True)
    for sub in subs:
        email_send(sub)
