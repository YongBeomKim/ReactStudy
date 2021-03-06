"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key & don't run with debug in production!
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
# Development & Production Mode Setting
if socket.gethostname() == 'pop-os':
    with open(os.path.join(BASE_DIR, '_key.json'), 'r') as f:
        SECRET_KEY = json.loads(f.read())['django']
    ALLOWED_HOSTS = ['*']
    DEBUG = True

else:
    with open('/etc/_key.json', 'r') as f:
        SECRET_KEY = json.loads(f.read())['django']
    ALLOWED_HOSTS = [
        '0.0.0.0',
        'sikpan.kr',
        'momukji.com',
    ]
    DEBUG = False


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'django_extensions',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'drf_yasg',
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            # Assign the Template Tag file
            # https://docs.djangoproject.com/en/3.1/topics/templates/#module-django.template.backends.django
            'libraries':{
                'react': 'server.templatetags.react',
            }
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'


# Development & Production DataBase Setting
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
if socket.gethostname() == 'pop-os':
    settingDB = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

else:
    settingDB = {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'mysql.cnf'),
        }
    }

DATABASES = {'default': settingDB}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static & Media files (Webapck Bundle file & Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')


# Development & Production Static Folder Setting
if socket.gethostname() == 'pop-os':
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

else:
    # Whitenoise Staticfiles Setting
    # https://www.youtube.com/watch?v=qSrJt3UD9xk
    # $ python manage.py collectstatic
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # For the Production Deployments
    # {% load static %}
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Django Restful API Settings..
# Pagination & authentication scheme Setting
# https://www.django-rest-framework.org/api-guide/pagination/
# https://www.django-rest-framework.org/api-guide/authentication/
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 5,
#     'DEFAULT_FILTER_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackend'
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ],
#     # Restful Framework 속도정의
#     # https://www.django-rest-framework.org/api-guide/throttling/
#     'DEFAULT_THROTTLE_CLASSES': [
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.UserRateThrottle'
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '5/hour',  # 익명 사용자의 API 속도
#         'user': '20/hour', # 인증 사용자의 API 속도
#         #'game-categories': '30/hour'
#     }
# }


# # from django.contrib.auth.decorators import login_required
# # https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django
# LOGIN_URL = '/api-auth/login'
# LOGIN_REDIRECT_URL = '/api-auth/login'
