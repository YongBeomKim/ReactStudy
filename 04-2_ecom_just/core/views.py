from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from .models import Item, OrderItem, Order

# Create your views here.


def checkout(request):
    return render(request, "core/checkout.html")


class HomeView(ListView):
    r"""`functional view` change to `class view`
    content = {"items": Item.objects.all()}
    return render(request, "core/home.html", content)"""
    model = Item
    paginate_by = 10
    template_name = "core/home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "core/product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False
    )
    order_queryset = Order.objects.filter(user=request.user, ordered=False)

    if order_queryset.exists():
        order = order_queryset[0]

        # Checking the item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            # adding the Quantity
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
        else:
            # adding new item
            messages.info(request, "This Item was added to your cart.")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This Item was added to your cart.")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_queryset = Order.objects.filter(user=request.user, ordered=False)

    # filtering by `User`
    if order_queryset.exists():
        order = order_queryset[0]

        # Checking the `item` is in the `order`
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False
            )[0]
            order.items.remove(order_item)
            messages.warning(request, "This item was removed from your cart.")
        else:
            # add a message saying the User doesnt have an Order
            messages.warning(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug)

    else:
        # add a message saying the User doesnt have an Order
        messages.info(request, "You do not have an active order.")
        return redirect("core:product", slug=slug)
