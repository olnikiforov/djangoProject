"""Generics of API."""
from main.models import Book, Post
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


class BooksSerializer(serializers.ModelSerializer):
    """Serializer class."""

    class Meta:
        """Meeta class."""
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'category',
        )
