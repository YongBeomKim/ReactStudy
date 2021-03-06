"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import socket, json, os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
# 1) Developer Mode Setting
if socket.gethostname() == "pop-os":
    with open(os.path.join(BASE_DIR, "_key.json")) as f:
        SECRET_KEY = json.loads(f.read())["django"]
    ALLOWED_HOSTS = ["*"]
    DEBUG = True
    DATABASE_CONFIG = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }

# 2) Production Mode Setting
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
        "OPTIONS": {"read_default_file": os.path.join(BASE_DIR, "mysql.cnf")},
    }

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "whitenoise.runserver_nostatic",
    "django_extensions",
    "crispy_forms",
    # Social Login
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # Restful API Framework 3rd-party apps
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "drf_yasg",
    # User Created Apps
    "django_countries",
    "core.apps.CoreConfig",
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
        "rest_framework.permissions.IsAuthenticated",
        # "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # Sessions : Browsable API and the ability to log in & out.
        # TokenAuthentication : Using the 'rest_framework.authtoken'
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Database Setting
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {"default": DATABASE_CONFIG}

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

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # Template User Tags
            # https://docs.djangoproject.com/en/3.1/topics/templates/#module-django.template.backends.django
            "libraries": {
                "react": "server.templatetags.react",
                "markdown_md": "server.templatetags.markdown_md",
                "cart_template_tags": "server.templatetags.cart_template_tags",
            },
        },
    },
]


WSGI_APPLICATION = "server.wsgi.application"

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

# django-allauth Setting
# https://django-allauth.readthedocs.io/en/latest/installation.html
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# allauth default setting.
# https://wayhome25.github.io/django/2017/05/18/django-auth/
SITE_ID = 1
AUTH_USER_MODEL = "auth.User"

# CRISPY FORMS
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Stripe API Token
# https://stripe.com/docs/api/charges/create?lang=python
STRIPE_PUBLIC_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#     }
# }

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
        # "LOCATION": os.path.join(BASE_DIR, ".cache"),
    }
}


# Static (Webapck Bundle file & Images), Static & Media folder is Merged.
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media")


# Development & Production Static Folder Setting
if socket.gethostname() == "pop-os":

    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    # Optionally provide a prefix as (prefix, path) tuples,
    # [("style", BASE_DIR / "static/css")]


else:
    # Using Whitenoise Staticfiles Setting.
    # https://www.youtube.com/watch?v=qSrJt3UD9xk
    # $ python manage.py collectstatic
    STATIC_URL = "/static/"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATIC_ROOT = [os.path.join(BASE_DIR, "staticfiles")]


if DEBUG:
    # And Adding the Django Debug Tools
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = "127.0.0.1"


# # from django.contrib.auth.decorators import login_required
# # https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django
# LOGIN_URL = '/api-auth/login'
# LOGIN_REDIRECT_URL = '/api-auth/login'
# LOGIN_URL = "/admin/login"
# LOGOUT_URL = "/"
# LOGIN_REDIRECT_URL = "/admin/login"
LOGIN_REDIRECT_URL = "/"
