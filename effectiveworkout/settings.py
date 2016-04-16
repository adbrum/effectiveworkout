"""
Django settings for effectiveworkout project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import tempfile
import importlib
import sys

from decouple import config, Csv
from dj_database_url import parse as dburl

TEMP_DIR = tempfile.mkdtemp()

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': TEMP_DIR,
    }
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

TIME= 600
SESSION_COOKIE_AGE = TIME
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_IDLE_TIMEOUT = TIME

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'effectiveworkout.core',
    'effectiveworkout.usersprofiles',
    'effectiveworkout.externalapplication',
    'effectiveworkout.assiduousness',
    'effectiveworkout.reviewsphysicals',
    'effectiveworkout.administration',
    'effectiveworkout.monthlyplans',
    'effectiveworkout.healthanamnese',
    'effectiveworkout.config',
    'effectiveworkout.utils',
    'effectiveworkout.exercises',

]

#Inclui apps do sistema no INSTALLD_APPS
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DIR_NAME = os.path.split(os.path.abspath(PROJECT_ROOT))
# APP_DIRS = os.listdir(PROJECT_ROOT)
#
# APP = ([file for file in APP_DIRS if not (file.startswith('.') or file.startswith('__') or file.endswith('.py'))])
# ######
#
# for app in APP:
#     INSTALLED_APPS.append(DIR_NAME[1] + '.' + app)

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
FIXTURE_DIRS = (
   os.path.join(PROJECT_DIR, '/fixtures/'),
)

LOGIN_URL = '/login/'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'effectiveworkout.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'effectiveworkout.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

defaut_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=defaut_dburl, cast=dburl),
}

#
# Easy thumbnails
#
THUMBNAIL_ALIASES = {
    '': {
        'micro': {'size': (30, 30)},
        'micro_cropped': {'size': (30, 30), 'crop': 'smart'},

        'thumbnail': {'size': (80, 80)},
        'thumbnail_cropped': {'size': (80, 80), 'crop': 'smart'},

        'small': {'size': (200, 200)},
        'small_cropped': {'size': (200, 200), 'crop': 'smart'},

        'medium': {'size': (400, 400)},
        'medium_cropped': {'size': (400, 400), 'crop': 'smart'},

        'large': {'size': (800, 800), 'quality': 90},
        'large_cropped': {'size': (800, 800), 'crop': 'smart', 'quality': 90},
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'core/static/media/')
MEDIA_URL = 'http://127.0.0.1:8000/static/media/'



# print('BASEDIR', BASE_DIR)
# print('PROJECT_ROOT', PROJECT_DIR)