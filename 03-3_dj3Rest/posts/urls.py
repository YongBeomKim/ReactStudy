from django.urls import path
from .views import PostList, PostDetail

app_name = "posts"
urlpatterns = [
    path("api/", PostList.as_view(), name="list"),
    path("api/<int:pk>", PostDetail.as_view(), name="detail"),
]
