from django.contrib import admin
from django.urls import path, include
from .routers import router
from .views import HomeView, index, home, export_json
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',       home,        name='home'),
    path('json',   export_json, name='apex_json'),
    # routers.py 에서 /article 경로 앞에 /api를 덧붙인다
    # /api/article 경로로 mapping이 완료된다
    path('api/', include(router.urls)),
    path('rss/',  include('rss.urls')),
    path('crud/', include('crud.urls')),
    path('crudjs/', include('crudjs.urls', namespace='crud')),
    #path('snippets/', include('snippets.urls', namespace='snippets')),
    # path('polls/', include('polls.urls', namespace='polls')),
    path('excel/', include('excel.urls', namespace='excel')),
    path('filter/', include('filter.urls', namespace='filter')),
    path('search/', include('search.urls', namespace='search')),
]
