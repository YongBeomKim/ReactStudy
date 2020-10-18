from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostFeaturedView,
    BlogPostCategoryView,
)


app_name = "blog"
urlpatterns = [
    path("", BlogPostListView.as_view(), name="list"),
    path("featured", BlogPostFeaturedView.as_view(), name="featured"),
    path("category", BlogPostCategoryView.as_view(), name="category"),
    path("<slug>", BlogPostDetailView.as_view(), name="slug"),
]
