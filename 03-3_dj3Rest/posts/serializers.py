from rest_framework import serializers
from .models import Post

# Access the Registered User Table
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created_at")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )

