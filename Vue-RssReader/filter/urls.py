from django.urls import re_path, path
from .views import PersonListView, PersonDetailView, content, snippet_detail
app_name="filter"

urlpatterns = [
    path('test/', content, name='content'),
    path('snippet/', snippet_detail),
    path('', PersonListView.as_view(), name='list'),
    path('<int:pk>/', PersonDetailView.as_view, name='detail')
]
