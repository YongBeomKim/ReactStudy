from django.urls import path, include
from .views import pizza, burger

app_name = "food"
urlpatterns = [
    path("pizza", pizza, name="pizza"),
    path("burger", burger, name="burger"),
]
