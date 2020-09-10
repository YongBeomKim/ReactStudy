from django.urls import path
from . import views

app_name = "mytube"
urlpatterns = [
    path("", views.VideoListView.as_view(), name="list"),
    path("new/", views.VideoCreateView.as_view(), name="new"),
    path("<int:pk>/", views.VideoDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.VideoUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.VideoDeleteView.as_view(), name="delete"),
    path(
        "<int:video_pk>/comments/new/",
        views.CommentCreateView.as_view(),
        name="new_comment",
    ),
]
