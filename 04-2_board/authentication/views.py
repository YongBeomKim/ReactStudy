from django.shortcuts import render

# Create your views here.
from django.views import View
import json
from django.http import JsonResponse


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data["username"]

        if not str(username).isalnum():
            return JsonResponse(
                {
                    "username_error": "username should only contain alphanumerix characters"
                }
            )
        return JsonResponse({"username_valid": True})


class RegistrationView(View):
    def get(self, request):
        return render(request, "auth/register.html")

