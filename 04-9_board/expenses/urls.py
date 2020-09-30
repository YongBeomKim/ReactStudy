from django.urls import path
from .views import index, add_expense

app_name = "expenses"
urlpatterns = [
    path("", index, name="add"),
    path("add", add_expense, name="add-expenses"),
]
