from django.urls import path

# main, ajax,
from .views import AjaxHandlerView, reactApi, reactAjax

app_name = "ajax"
urlpatterns = [
    # path("", main, name="main"),
    # path("ajax", ajax, name="ajax"),
    path("", AjaxHandlerView.as_view(), name="index"),
    path("react", reactAjax, name="react"),
    path("api", reactApi, name="api"),
]
