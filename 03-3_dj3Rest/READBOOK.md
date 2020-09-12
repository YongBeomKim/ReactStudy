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
