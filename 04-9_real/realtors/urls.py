from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView

app_name = "realtor"
urlpatterns = [
    path("", RealtorListView.as_view(), name="list"),
    path("<int:pk>/", RealtorView.as_view(), name="detail"),
    path("topseller/", TopSellerView.as_view(), name="top-list"),
]