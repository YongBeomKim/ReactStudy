## Django3 for API

## Chapter 1: Web APIs

### URL

- scheme : https
- a hostname : www.django.com
- an optional path : /admin/

### HTTP Verbs

- Use : `POST`
- Read : `GET`
- Update : `PUT`
- Delete : `DELETE`

### End Points

`https://www.mysite.com/api/user/<id>`

### HTTP

Fllow Text is the body message with **HTTP responses** containing data

```r
Diagram
HTTP/1.1 200 OK
Date: Wed, 17 Feb 2020 23:26:07 GMT
Server: gws
Accept-Ranges: bytes
Content-Length: 13
Content-Type: text/html; charset=UTF-8

Hello, world!
```

### Status

most common ones such as 200 (OK), 201 (Created), 301(Moved Permanently), 404 (Not Found), and 500 (Server Error)

HTTP request: it worked (2xx), it was redirectedsomehow (3xx), the client made an error (4xx), or the server made an error (5xx).

- 2xx Success
- 3xx Redirection
- 4xx Client Error
- 5xx Server Error

<br/>

## Chapter 2: Django Library and API

### Traditional Django

A traditional Django website consists of a **single projectand** one (or more)apps representing discrete(clearly separate or different in shape or form) functionality.

### Django REST Framework

The `api` app will not have its **own database models** and will expose a **single endpoint** that lists out all books in JSON. There are **multiple ways we can organize these files** however my preferred approachis to create a dedicated `api` app

<br/>

## Chapter 7: User Authentication

### JSON Web Tokens (JWTs).

**HTTP** is a **stateless protocol** so Each time a user requests a restricted resource it must verify itself. The solution is to pass along a **unique identifier with each HTTP request.**

**Django REST Framework** ships with **four** different built-in authentication options: `basic`, `session`, `token` and `default`. And there are many more third-party packages that offer additional features like `JSON Web Tokens` (JWTs).

```r
<Client>
-------->
GET / HTTP/1.1
                           <Server>
    <------------------------------
          HTTP/1.1 401 Unauthorized
            WWW-Authenticate: Basic

<Client>
-------->
GET / HTTP/1.1
Authorization: Token 401f7ac837da42
( unencrypted base64 encoded )

                           <Server>
    <------------------------------
                    HTTP/1.1 200 OK
```

Django REST Frameworks’ built-in `TokenAuthentication` is deliberately quite basic. `JSON Web Tokens` (JWTs) are a new, enhanced version of tokens that can be added to Django REST Framework via **several third-party package**. JWTs have several benefits including the ability to **generate unique client tokens** and **token expiration** with a third-party service like `Auth0`.

### Default Authentication

`DEFAULT-PERMISSION-CLASSES` was set to `AllowAny` before we updated it to `IsAuthenticated`.The `DEFAULT_AUTHENTICATION_CLASSES` are set by default to `SessionAuthentication` and `BasicAuthentication` in `settings.py` file.

### Auth Token & EndPoints

We will use `dj-rest-auth` in combination with `django-allauth` to simplify things. Make sure to note that **URLs** should have a **dash-** not an underscore \_, which is an easy mistake to make.

```r
$ pip install django-rest-auth
$ pip install dj-rest-auth

# $ pip install django-allauth
# $ pip install djangorestframework-simplejwt
```

### User Registration

Then update our `INSTALLED_APPS` setting. We must add several new configs `django.contrib.sites`, `allauth`, `allauth.account`, `allauth.socialaccount`, `dj_rest_auth.registration`

```python
# settings.py
INSTALLED_APPS = [
  ...
  'django.contrib.sites',

  # 3rd-party apps
  'rest_framework',
  'rest_framework.authtoken',
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  'dj_rest_auth',
  'dj_rest_auth.registration',
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1

```

`REST_FRAMEWORK` setting is 1) Sessions : Browsable API and the ability to log in & out. 2) BasicAuthentication : `rest_framework.authentication.BasicAuthentication` is pass the session ID in HTTP headers but not Using this time, 3) TokenAuthentication : Using the 'rest_framework.authtoken' POST API.

<br/>

## Chapter 8: Viewsets and Routers

### Viewsets

**Viewset** is a way to combine the logic for **multiple related views** into **a single class**. Almost the same as View classes, except operations **read** & **update**, not get & put.

- **[ViewSet's url pattern names](https://kimdoky.github.io/django/2018/07/08/drf-Routers/)**
- **[get_user_model()'s Django Document](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model)**

```python
# views.py
# Create your views here.
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
```

### Routers

Django REST Framework has `SimpleRouter` and `DefaultRouter`. **SimpleRouter** is possible to create custom routers for more advanced functionality.

```python
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

app_name = "posts"
router = SimpleRouter()

# URL PATTERN NAME : posts:post-list, post:post-detail
router.register("", PostViewSet, basename="post")

# URL PATTERN NAME : posts:user-list, posts:user-detail
router.register("user", UserViewSet, basename="user")
urlpatterns = router.urls
```

if your not define the `basename` then DRF is designate automatically URL PATTERN names. folloing is the sample of the names.

```r
URL path: ^users/$          URL Pattern Name: 'user-list'
URL path: ^users/{pk}/$     URL Pattern Name: 'user-detail'
URL path: ^accounts/$       URL Pattern Name: 'account-list'
URL path: ^accounts/{pk}/$  URL Pattern Name: 'account-detail'
```

<br/>

## Chapter 9: Schemas and Documentation

**Schema** is a machine-readable document that outlines all available API. **Documentation** is something to makes it easier **for humans to read**.

### Schemas

Over the version 3.9, Django REST Framework switched firmly over to the OpenAPI(as Swagger) schema. Following will let us render our schema in the commonly used `YAML-based` OpenAPI format.

```r
$ pip install pyyaml
$ pip install drf-yasg (OpenAPI decoing Module)
$ python manage.py generateschema > openapi-schema.yml
```

If you open that file it’s quite long and not very human-friendly. But to a computer,it’s perfectly formatted

```python
from rest_framework.schemas import get_schema_view

urlpatterns = [
    ...
    path("openapi/",
        get_schema_view(
            title="Blog API",
            description="A sample API for learning DRF",
            version="1.0.0",
        ), name="openapi-schema", ),
]
```

### Documentation

Adding the 'drf_yasg' in the `INSTALLED_APPS = []`, we can replace DRF’s `get_schema_view` with the one from `drf_yasg` as well as importing `openapi`. Also add `DRF’s permission` for additional options.
