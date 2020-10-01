from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Item

# Create your views here.


def checkout(request):
    return render(request, "core/checkout.html")


class HomeView(ListView):
    r"""`functional view` change to `class view`
    content = {"items": Item.objects.all()}
    return render(request, "core/home.html", content)"""
    model = Item
    template_name = "core/home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "core/product.html"
