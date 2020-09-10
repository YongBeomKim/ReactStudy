import os
import socket

# secret key 설정을 환경변수 별로 적용
if socket.gethostname() == "pop-os":
    with BASE_DIR.joinpath("_key.json") as f:
        SECRET_KEY = json.loads(f.open().read())["django"]
    ALLOWED_HOSTS = ["*"]
    DEBUG = True

else:
    with open("/etc/_key.json", "r") as f:
        SECRET_KEY = json.loads(f.read())["django"]
    ALLOWED_HOSTS = [
        "0.0.0.0",
        "sikpan.kr",
        "momukji.com",
    ]
    DEBUG = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'corsheaders',
    # 'bootstrap3',
    'bootstrapform',
    'widget_tweaks',
    # 'graphene_django',
    'crispy_forms',
    'django_tables2',  # django_tables2
    'django_filters',  # table 에서 검색폼 만들기
    'rss.apps.RssConfig',
    'crud.apps.CrudConfig',
    'crudjs.apps.CrudjsConfig',
    # 'polls.apps.PollsConfig',
    'excel.apps.ExcelConfig',
    'filter.apps.FilterConfig',
    'search.apps.SearchConfig',
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'
# CRISPY_TEMPLATE_PACK = 'uni_form'

# 로그 기록의 설정을 활성화 한다
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'mylogger': {
            'handlers': ['console'],
            'level': 'INFO'
        },
    },
}

# # REST API설정 (필터, 페이징)
# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 5
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # CORSHEADER 를 제한합니다
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.security.SecurityMiddleware',  # https 보안설정
]

CORS_ORIGIN_ALLOW_ALL = True

# https 보안설정 활성화
# SECURE_SSL_REDIRECT = True
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

# 개발자 환경에서는 STATICFILES_DIRS 로 정적폴더를 Url과 연결이 필수다!!
if socket.gethostname() == 'markbaum':
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    # 웹 서버에서는 보다 구체적인 설정을 필요로 한다
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ROOT_URLCONF = 'server.urls'
WSGI_APPLICATION = 'server.wsgi.application'

TEMPLATES = [
    {'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.request', # django-table2
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages', ], }, }, ]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False
