from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets  # ,generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# # ListCreateAPIView : read-write endpoint
# class PostList(generics.ListCreateAPIView):
#     # permission_classes : Only autherized user allowed.
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# # RetrieveUpdateDestroyAPIView : read update & delete endpoint
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes : Only autherized user allowed.
#     # permission_classes = (permissions.IsAuthenticated,)
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView):
#     permission_class = (IsAuthorOrReadOnly,)
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
