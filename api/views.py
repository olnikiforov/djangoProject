"""View file of API."""

from api.generics import BooksSerializer, PostSerializer
from main.models import Book, Post
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class PostAPIViewSet(viewsets.ModelViewSet):
    """Post API ViewSet."""

    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination



class BooksAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BooksSerializer
    pagination_class = PageNumberPagination