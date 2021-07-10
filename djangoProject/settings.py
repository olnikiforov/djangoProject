"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import mimetypes
import os
from pathlib import Path

from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '*f9&r-fv4nglp!je_77o_a%gy6@y(-4-j&o_krtsw_nj-*ywrk'

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
#
#ALLOWED_HOSTS = ['*']


DEBUG = os.environ.get('DEBUG_MODE') == '1'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(':')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'main',
    'account',
    'django_extensions',
]

CACHE = {
    'default': {
        'LOCATION': 'memcached:11211',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'main.middleware.SimpleMiddleware',
    'main.middleware.LogMiddleware',
]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'account.user'

INTERNAL_IPS = [
    '127.0.0.1',
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/html", ".css", True)



STATIC_URL = '/static/'

DOMAIN = 'http://0.0.0.0:8000'

LOGIN_REDIRECT_URL = '/'


# Celery


CELERY_BROKER_URL = 'amqp://{0}:{1}@{2}:5672'.format(
    os.environ.get('RABBITMQ_DEFAULT_USER', "guest"),
    os.environ.get('RABBITMQ_DEFAULT_PASS', "guest"),
    os.environ.get('RABBITMQ_DEFAULT_HOST', "localhost"),
)

CELERY_TIMEZONE = 'Europe/Kiev'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BEAT_SCHEDULE = {
    'delete_logs_async': {
        'task': 'main.tasks.delete_logs',
        'schedule': crontab(minute=0, hour=1),
    },
    'notify_subscribers': {
        'task': 'main.tasks.subscribers_notify',
        'schedule': crontab(minute=0, hour=9),
    },
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static')
]

#STATIC_ROOT = os.path.join(BASE_DIR, '', 'static_content', 'static')

STATIC_ROOT = os.path.join('/tmp', 'static_content', 'static')

if DEBUG:
    import socket

    DEBUG_TOOLBAR_PATCH_SETTINGS = True
    INTERNAL_IPS = [socket.gethostbyname(socket.gethostname())[:-1] + '1']
