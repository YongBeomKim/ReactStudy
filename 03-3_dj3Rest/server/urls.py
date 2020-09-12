"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("api/", api, name="api"),
    path("api-auth/", include("rest_framework.urls")),
    # Implement your own user authentication endpoints
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("todos/", include("todos.urls")),
    path("posts/", include("posts.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Adding Django Debug Tools
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

import debug_toolbar

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

