from django.urls import path

from .views import BootstrapFilterView

app_name = "core"
urlpatterns = [path("", BootstrapFilterView, name="index")]
