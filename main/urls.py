"""Urls of site."""
# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('post/create', views.post_create, name='post_create'),
    path('api/post', views.post_api, name='api_post'),
    path('posts/subscribe', views.posts_subscribe, name='posts_subscribe'),
    path('api/subscribe', views.api_subscribe, name='api_subscribe'),
]
