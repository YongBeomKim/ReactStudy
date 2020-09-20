from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.views import View
from django.http import JsonResponse

# Create your views here.
from validate_email import validate_email
import json


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data["username"]

        # .isalnum()
        # 1) True : all characters in the string are alphanumeric
        # https://www.programiz.com/python-programming/methods/string/isalnum
        if not str(username).isalnum():
            return JsonResponse(
                {
                    "username_error": "username should only contain alphanumerix characters"
                }
            )
        return JsonResponse({"username_valid": True})


class EmilValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data["email"]

        # .isalnum()
        # 1) True : all characters in the string are alphanumeric
        # https://www.programiz.com/python-programming/methods/string/isalnum
        if not validate_email(email):
            return JsonResponse({"email_error": "Email is invald"}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({"email_error": "sorry email is already used"})
        return JsonResponse({"email_valid": True})


class RegistrationView(View):
    def get(self, request):
        return render(request, "auth/register.html")


class LoginView(View):
    def get(self, request):
        return render(request, "auth/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(
                        request, "Welcome, " + user.username + " you are now logged in"
                    )
                    return
                messages.error(request, "Account is not active,please check your email")
                return render(request, "authentication/login.html")
            messages.error(request, "Invalid credentials,try again")
            return render(request, "authentication/login.html")

        messages.error(request, "Please fill all fields")
        return render(request, "auth/login.html")

