from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import Contact


class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        try:
            send_mail(
                data["subject"],
                # Message
                "Name: "
                + data["name"]
                + "\nEmail: "
                + data["email"]
                + "\n\nMessage:\n"
                + data["message"],
                # User Data
                "momukjilab@gmail.com",
                ["momukjilab@gmail.com"],
                fail_silently=False,
            )
            contact = Contact(
                name=data["name"],
                email=data["email"],
                subject=data["subject"],
                message=data["message"],
            )
            contact.save()
            return Response({"success": "Message sent successfully"})
        except:
            return Response({"error": "Message failed"})

