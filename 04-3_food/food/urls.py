from django.urls import path, include
from .views import index

app_name = "food"
urlpatterns = [
    path("", index, name="pizza"),
]
