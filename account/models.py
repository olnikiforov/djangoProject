"""Account models."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Class User."""

    email = models.EmailField('Email address', blank=False, null=False, unique=True)
