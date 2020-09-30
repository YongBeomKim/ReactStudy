from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import (
    RegistrationView,
    UsernameValidationView,
    EmilValidationView,
    LoginView,
)

app_name = "auth"
urlpatterns = [
    path("register", RegistrationView.as_view(), name="register"),
    path("username", csrf_exempt(UsernameValidationView.as_view()), name="username"),
    path("email", csrf_exempt(EmilValidationView.as_view()), name="email"),
    path("login", LoginView.as_view(), name="login"),
]
