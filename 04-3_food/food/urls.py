from django.urls import path, include
from .views import pizza, burger, order, success, signup, loginpage, logoutpage

app_name = "food"
urlpatterns = [
    path("pizza", pizza, name="pizza"),
    path("burger", burger, name="burger"),
    path("order", order, name="order"),
    path("success", success, name="success"),
    path("signup", signup, name="signup"),
    path("login", loginpage, name="login"),
    path("logout", logoutpage, name="logout"),
]
