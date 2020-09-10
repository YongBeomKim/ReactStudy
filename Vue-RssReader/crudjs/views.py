from django.shortcuts import render, redirect
from .models import Member
# Create your views here.


def index(request):
    return render(request, 'crudjs/index.html')

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect("crud:index")

def read(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crudjs/result.html', context)

def filter(request, data):
    members = Member.objects.filter(firstname=data)
    context = {'members': members}
    return render(request, 'crudjs/result.html', context)


def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'member': members}
    return render(request, 'crudjs/edit.html', context)


def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname  = request.POST['lastname']
    member.save()
    return redirect("crud:index")


def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect("crud:index")



