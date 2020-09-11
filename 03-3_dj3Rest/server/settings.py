"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import socket, json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
if socket.gethostname() == "pop-os":
    with BASE_DIR.joinpath("_key.json") as f:
        SECRET_KEY = json.loads(f.open().read())["django"]
    ALLOWED_HOSTS = ["*"]
    DEBUG = True
    DATABASE_CONFIG = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }

else:
    with open("/etc/_key.json", "r") as f:
        SECRET_KEY = json.loads(f.read())["django"]
    ALLOWED_HOSTS = [
        "0.0.0.0",
        "sikpan.kr",
        "momukji.com",
    ]
    DEBUG = False
    DATABASE_CONFIG = {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {"read_default_file": BASE_DIR / "mysql.cnf"},
    }

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    "django_extensions",
    "bootstrap4",
    "rest_framework",
    # 'rest_framework.authtoken',
    # 'drf_yasg',
    "todos.apps.TodosConfig",
    "posts.apps.PostsConfig",
]

# React.js Rest Framework Setting..
# https://www.django-rest-framework.org/api-guide/settings/

# "DEFAULT_PERMISSION_CLASSES" Settings..
# • AllowAny : any user, authenticated or not, has full access
# • IsAuthenticated : only authenticated, registered users have access
# • IsAdminUser : only admins/superusers have access
# • IsAuthenticatedOrReadOnly : unauthorized users can view, but
#       only authenticated users have write, edit, or delete privileges
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.AllowAny",
    ]
}

MIDDLEWARE = [
    # "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Adding the Django Debug Tools
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
if socket.gethostname() == "pop-os":
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = "127.0.0.1"


ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # Assign the Template Tag file
            # https://docs.djangoproject.com/en/3.1/topics/templates/#module-django.template.backends.django
            "libraries": {
                "react": "server.templatetags.react",
                "markdown_md": "server.templatetags.markdown_md",
            },
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"

# Database Setting
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {"default": DATABASE_CONFIG}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Django Cache Framework
# https://docs.djangoproject.com/en/3.1/topics/cache/
CACHES = {
    "default": {
        # >> Local-memory caching
        # https://docs.djangoproject.com/en/3.1/topics/cache/#local-memory-caching
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-store",
        # >> Memory Cache Acivated Option
        # "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        # 'LOCATION': '127.0.0.1:11211',
        # >> DataBase Cache Acivated Options
        # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 'LOCATION': 'my_cache_table',
        # >> FileBased Cache Activated Option
        # "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        # "LOCATION": BASE_DIR.joinpath(".cache"),
    }
}


# Static (Webapck Bundle file & Images)
# Static & Media folder is Merged.
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "static/media"


# Development & Production Static Folder Setting
if socket.gethostname() == "pop-os":
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
        (BASE_DIR / "static"),
    ]
    # Optionally provide a prefix as (prefix, path) tuples,
    # ("style", BASE_DIR / "static/css")]

else:
    # Whitenoise Staticfiles Setting
    # https://www.youtube.com/watch?v=qSrJt3UD9xk
    # $ python manage.py collectstatic
    STATIC_URL = "/static/"
    STATIC_ROOT = [BASE_DIR / "staticfiles"]
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # from django.contrib.auth.decorators import login_required
# # https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django
# LOGIN_URL = '/api-auth/login'
# LOGIN_REDIRECT_URL = '/api-auth/login'
LOGIN_URL = "/admin/login"
LOGOUT_URL = "/"
LOGIN_REDIRECT_URL = "/admin/login"
