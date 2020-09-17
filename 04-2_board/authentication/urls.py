from django.urls import path
from .views import RegistrationView, UsernameValidationView


app_name = "auth"
urlpatterns = [
    path("register", RegistrationView.as_view(), name="register"),
    path("validation", UsernameValidationView.as_view(), name="validate"),
]
