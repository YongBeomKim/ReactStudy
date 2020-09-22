from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Pizza, Buger


def pizza(request):
    pizzas = Pizza.objects.all()
    content = {
        "pizzas": pizzas,
        "active_link": "pizza",
    }
    return render(request, "food/pizza.html", content)


def burger(request):
    burgers = Buger.objects.all()
    content = {
        "burgers": burgers,
        "active_link": "burger",
    }
    return render(request, "food/burger.html", content)
