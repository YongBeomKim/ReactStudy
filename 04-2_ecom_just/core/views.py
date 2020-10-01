from django.shortcuts import render
from .models import Item

# Create your views here.


def item_list(request):
    content = {"items": Item.objects.all()}
    return render(request, "home-page.html", content)
