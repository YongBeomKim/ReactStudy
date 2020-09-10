from django.shortcuts import render


def index(request):
    content = {}
    return render(request, "home.html", content)
