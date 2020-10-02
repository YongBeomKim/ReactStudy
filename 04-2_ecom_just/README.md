# Project ECOMMERCE

![Django badge](https://img.shields.io/badge/Django-3.1-blue.svg)

## Introduction

ECOMMERCE Django Project is from the [JUST DJANGO](https://www.youtube.com/playlist?list=PLLRM7ROnmA9F2vBXypzzplFjcHUaKWWP5)'s YouTube Tutorial. and the Coding Source is from the [GitHub](https://github.com/justdjango/django-ecommerce)

Source code is from the Django 2 version, Django 3 version is seperated the name is **[django-simple-ecommerce](https://github.com/justdjango/django-simple-ecommerce)**

And Next Step is using React in the front end sides. [YouTube Tutorial](https://www.youtube.com/playlist?list=PLLRM7ROnmA9Hp8j_1NRCK6pNVFfSf4G7a) & [GitSource](https://github.com/justdjango/django-react-ecommerce) is under the links.

[![Build an Ecommerce Website with Django](https://i.ytimg.com/vi/z4USlooVXG0/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLA8QhBJLQ2nI0omuhdYdfUR9QjPTg)](https://www.youtube.com/playlist?list=PLLRM7ROnmA9F2vBXypzzplFjcHUaKWWP5)

<br/>

# **Django Scripts and Tips**

<br/>

## Rename the Setting Folder

following scripe can change the code related with setting folder.

`$ python manage.py rename <change name>`

<br/>

## Django Message Tags

You can get more infomation at the [Django Project site](https://docs.djangoproject.com/en/3.1/ref/contrib/messages/)

|  Level  | Constant Tag |
| :-----: | :----------: |
|  DEBUG  |    debug     |
|  INFO   |     info     |
| SUCCESS |   success    |
| WARNING |   warning    |
|  ERROR  |    error     |

<br/>

## Template can get tuple's second queryset

**[Django get the Category's second data](https://ssungkang.tistory.com/entry/Django-ChoiceField-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)** In this case, you want call the Tuple's first data is not easy to know what it is. then you can call the tuple's second data by following code.

`get_{fieldname}_display`

<br/>

## reverse() & redirect()

`redirect()` using Model's function.

```python
# views.py
from django.shortcuts import redirect

def index(request, slug):
    return redirect("core:product", slug=slug)
```

`reverse()` is using view function,

```python
# models.py
from django.shortcuts import reverse

class Database(models.Model):
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("core:list", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("core:cart", kwargs={"slug": self.slug})
```

<br/>

## The Process of Git Sources

- **[django2 project boilerplate](https://github.com/justdjango/django_project_boilerplate)**
- **[django2 ecommerce](https://github.com/justdjango/django-ecommerce)**
- **[django3 simple ecommerce](https://github.com/justdjango/django-react-ecommerce)**
- **[django-react-boilerplate](https://github.com/justdjango/django-react-boilerplate)**

<br/>

## Sites

- **[MDBootstrap Table](https://mdbootstrap.com/docs/jquery/tables/basic/)**
- **[MDBootstrap Tab Component](https://mdbootstrap.com/docs/jquery/components/tabs/)**
- **[MDBootstrap Icons](https://mdbootstrap.com/docs/jquery/content/icons-list/)**
- **[MDBootstrap E-commerce GitHub](https://github.com/mdbootstrap/Ecommerce-Template-Bootstrap)**
- **[django-rest-framework-simplejwt](https://github.com/SimpleJWT/django-rest-framework-simplejwt)**
- **[django allauth template](https://github.com/pennersr/django-allauth/tree/master/allauth/templates)**
