from django.urls import path
from .views import ListTodo, DetailTodo

app_name = "todos"
urlpatterns = [
    path("", ListTodo.as_view(), name="list"),
    path("<int:pk>/", DetailTodo.as_view(), name="detail"),
]
