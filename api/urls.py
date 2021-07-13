"""API urls."""

from rest_framework.routers import DefaultRouter
from .views import BooksAPIViewSet, PostAPIViewSet

from . import views

router = DefaultRouter()
router.register(prefix='posts', viewset=views.PostAPIViewSet, basename='post')
router.register(prefix='books_view', viewset=BooksAPIViewSet, basename='book')

urlpatterns = router.urls
