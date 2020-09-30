from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


User = get_user_model()


class SignupView(APIView):
    permissions_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        name = data["name"]
        email = data["email"]
        password = data["password"]
        password2 = data["password2"]
        if password == password2:
            # Validation check 01 : exist mail
            if User.objects.filter(email=email).exists():
                return Response({"error": "Email already exists."})
            else:
                # Validation check 02 : Password charactor is too short
                if len(password) < 6:
                    return Response({"error": "Password must be at least 6 characters"})
                else:
                    # Passed the check list
                    user = User.objects.create_user(
                        email=email, password=password, name=name,
                    )
                    user.save()
                    return Response({"success": "User created successfully"})
        else:
            # Validation check 03 : password not Matched
            return Response({"error": "Password do not match"})

