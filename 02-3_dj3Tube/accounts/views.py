from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse


# Create your Generic (signup, login, logout) Form view Instance

signup = CreateView.as_view(
    form_class=UserCreationForm,
    success_url=settings.LOGIN_URL,
    template_name="form.html",
)

login = LoginView.as_view(template_name="form.html")

logout = LogoutView.as_view(next_page=settings.LOGOUT_URL)


@login_required
def profile(request):
    return render(request, "accounts/profile.html")
