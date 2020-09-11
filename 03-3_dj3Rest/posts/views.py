from django.shortcuts import render

# Create your views here.
from rest_framework import generics  # , permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


# ListCreateAPIView : read-write endpoint
class PostList(generics.ListCreateAPIView):

    # permission_classes : Only autherized user allowed.
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# RetrieveUpdateDestroyAPIView : read update & delete endpoint
class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    # permission_classes : Only autherized user allowed.
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
