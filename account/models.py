"""Account models."""
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Class User."""

    email = models.EmailField('Email address', blank=False, null=False, unique=True)
    confirmation_token = models.UUIDField(default=uuid.uuid4)


def user_ava_upload(instance, filename):
    """Upload avatar."""
    return f'{instance.user_id}/{filename}'


class Ava(models.Model):
    """Class avatar."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.ImageField(upload_to=user_ava_upload)


class Profile(models.Model):
    """Class profile."""

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to=user_ava_upload)

    def __str__(self):
        """Str method."""
        return str(self.user)
