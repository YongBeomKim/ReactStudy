from django.shortcuts import render

def index_scss(request):
    return render(request, "scssTest.html")

def home(request):
    return render(request, "home.html")