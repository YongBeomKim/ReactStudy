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