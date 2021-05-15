"""Urls of site."""
# from django.contrib import admin
from django.urls import path
from django.views.decorators import cache
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path('', views.index, name='homepage'),
    path('', TemplateView.as_view(template_name='main/index.html'), name='homepage'),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon/favicon.ico')),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('post/create', views.post_create, name='post_create'),
    path('posts/update/<int:post_id>', views.post_update, name='post_update'),
    path('posts/<int:post_id>', views.post_show, name='post_show'),
    # path('posts/list/', views.PostsListView.as_view(), name='posts_list'),
    path('posts/all/', cache.cache_page(120)(views.PostsListView.as_view()), name='posts_list'),
    path('posts/list/xlsx', views.DownloadPostsXLSX.as_view(), name='posts_xlsx'),

    path('authors/new', views.authors_new, name='authors_new'),
    # path('authors/all', views.authors_all, name='authors_all'),
    path('authors/all', cache.cache_page(120)(views.authors_all), name='authors_all'),
    path('author/subscribe', views.author_subscribe, name='author_subscribe'),
    path('author/subscribers/all', views.author_subscribers_all, name='author_subscribers_all'),

    path('author/subscribers/notify', views.subscribers_notify, name='subscribers_notify'),

    path('books/all/', views.books, name='books'),
    # path('categories/all/', views.categories, name='categories'),
    path('categories/all/', cache.cache_page(120)(views.categories), name='categories'),

    path('contact-us/create/', views.ContactsView.as_view(), name='contact-us-create'),

    path('api/post', views.post_api, name='api_post'),
    path('api/subscribe', views.api_subscribe, name='api_subscribe'),
    path('api/authors/new', views.api_authors_new, name='api_authors_new'),
]
