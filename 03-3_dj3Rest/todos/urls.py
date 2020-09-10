from django.urls import path
from .views import ListTodo, DetailTodo, index

app_name = "todos"
urlpatterns = [
    path("", index, name="index"),
    path("api/", ListTodo.as_view(), name="list"),
    path("api/<int:pk>/", DetailTodo.as_view(), name="detail"),
]
