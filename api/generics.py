"""Generics of API."""
from main.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Class postSerializer."""

    class Meta:
        """Meta class."""

        model = Post
        fields = (
            'id',
            'title',
            'description',
            'content',
            'mood',
            'updated',
            'created',
            'get_mood_display'
        )
