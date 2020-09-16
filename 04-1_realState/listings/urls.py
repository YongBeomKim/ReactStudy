from django.urls import path
from .views import ListingsView, ListingView, SearchView

urlpatterns = [
    path("", ListingsView.as_view(), name="list"),
    path("<slug>/", ListingsView.as_view(), name="item"),
    path("search/", SearchView.as_view(), name="search"),
]
