from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Simplify the User Input Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from .forms import NewUserForm
from .models import Pizza, Buger, Item, Order
import json, random


def randomOrderNumber(length):
    # Order Number Auto Generator
    sample = "ABCDEFGH0123456789"
    numberOrder = "".join((random.choice(sample) for i in range(length)))
    return numberOrder


def pizza(request):
    request.session.set_expiry(0)
    pizzas = Pizza.objects.all()
    content = {
        "pizzas": pizzas,
        "active_link": "pizza",
    }
    return render(request, "food/pizza.html", content)


def burger(request):
    request.session.set_expiry(0)
    burgers = Buger.objects.all()
    content = {
        "burgers": burgers,
        "active_link": "burger",
    }
    return render(request, "food/burger.html", content)


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session["note"] = request.POST.get("note")
        request.session["orders"] = request.POST.get("orders")
        request.session["bill"] = request.POST.get("bill")
        randomNum = randomOrderNumber(6)

        # Session data Change to Json
        orders = json.loads(request.session["orders"])

        # Checking the Order Number is Unique.
        while Order.objects.filter(number=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)

        if request.user.is_authenticated:
            # Order Total Infomation
            order = Order(
                customer=request.user,
                number=randomOrderNumber(6),
                bill=float(request.session["bill"]),
                note=request.session["note"],
            )
            order.save()

            # Order content saved in session
            request.session["orderNum"] = order.number
            # Write Each Item Information.
            for eachItem in orders:
                item = Item(
                    order=order,
                    name=eachItem[0],
                    size=eachItem[1],
                    price=float(eachItem[2]),
                )
                item.save()

    content = {
        "active_link": "order",
    }

    return render(request, "food/order.html", content)


def success(request):
    orderNum = request.session["orderNum"]
    bill = request.session["bill"]
    items = Item.objects.filter(order__number=orderNum)
    content = {
        "orderNum": orderNum,
        "bill": bill,
        "items": items,
    }
    return render(request, "food/success.html", content)


def signup(request):
    content = {}
    if request.POST:
        # form = UserCreationForm(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            content["form"] = form
    else:
        # form = UserCreationForm(request.POST)
        form = NewUserForm(request.POST)
        content["form"] = form
    return render(request, "food/signup.html", content)


def loginpage(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"User Name: {username}\nPass Word: {password}")
        userinfo = authenticate(request, username=username, password=password)
        if userinfo is not None:
            login(request, userinfo)
            return redirect("index")
        else:
            messages.info(request, "username and/or password are incorrect")
    content = {"active_link": "login"}
    return render(request, "food/login.html", content)


def logoutpage(request):
    logout(request)
    return redirect("index")
