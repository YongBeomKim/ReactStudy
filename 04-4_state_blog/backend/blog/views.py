from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http import JsonResponse
from .models import BlogPost
from .serializers import BlogPostSerializer


# blog page list
class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by("-date_created")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permissions_classes = (permissions.AllowAny,)


# blog each page
class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by("-date_created")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permissions_classes = (permissions.AllowAny,)


#
class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permissions_classes = (permissions.AllowAny,)


class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permissions_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        category = data["category"]
        queryset = BlogPost.objects.order_by("-date_created").filter(
            category__iexact=category
        )
        serializer = BlogPostSerializer(queryset, many=True)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)
