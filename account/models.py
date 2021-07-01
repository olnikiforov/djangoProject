"""Account models."""
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Class User."""

    email = models.EmailField('Email address', blank=False, null=False, unique=True)
    confirmation_token = models.UUIDField(default=uuid.uuid4)
