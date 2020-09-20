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
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import index, profile, works


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("profile/", profile, name="profile"),
    path("works/", works, name="works"),
]

# Rest API
urlpatterns += [
    # path("api/", api, name="api"),
    path("api-auth/", include("rest_framework.urls")),
    # Implement your own User Authentication End points
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    # path("todos/", include("todos.urls")),
    # path("posts/", include("posts.urls")),
    # path(
    #     "openapi/",
    #     get_schema_view(  # new
    #         title="Blog API",
    #         description="A sample API for learning DRF",
    #         version="1.0.0",
    #     ),
    #     name="openapi-schema",
    # ),
]

# Adding the Django Rest Framework's Documents
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="A simple API for learning DRF",
        terms_of_service="https://policies.google.com/terms",
        contact=openapi.Contact(email="ybkim@momukji.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_kwargs=0), name="schema-doc"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Adding Django Debug Tools
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

import debug_toolbar

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

