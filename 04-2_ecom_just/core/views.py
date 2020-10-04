from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item, OrderItem, Order, BillingAddress
from .forms import CheckoutForm

# Create Payment api

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        content = {"form": form}
        print("GET Checking the process...")
        return render(self.request, "core/checkout.html", content)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                address_street = form.cleaned_data.get("address_street")
                address_apartment = form.cleaned_data.get("address_apartment")
                countries = form.cleaned_data.get("countries")
                zip_code = form.cleaned_data.get("zip_code")
                # same_billing_address = form.cleaned_data.get("same_billing_address")
                # save_info = form.cleaned_data.get("save_info")
                billing_address = BillingAddress(
                    user=self.request.user,
                    address_street=address_street,
                    address_apartment=address_apartment,
                    countries=countries,
                    zip_code=zip_code,
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                print("Checking the process...")
                payment_option = form.cleaned_data.get("payment_option")
                if payment_option == "S":
                    return redirect("core:payment", payment_option="stripe")
                elif payment_option == "P":
                    return redirect("core:payment", payment_option="paypal")
                else:
                    messages.warning(self.request, "Invalid payment option")
                    return redirect("core:checkout")

            else:
                print("Error Checking the process...")
                messages.warning(self.request, "Failed checkout")
                return redirect("core:checkout")

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("core:order-summary")


class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        content = {
            "order": order,
        }
        return render(self.request, "core/payment.html", content)

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)

        # `source` is obtained with Stripe.js
        # https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token
        token = self.request.POST.get("stripeToken")
        amount = order.get_total() * 100  # by cents

        # Stripe API Error Handling
        # https://stripe.com/docs/api/errors/handling?lang=python
        try:
            charge = stripe.Charge.create(amount=amount, currency="usd", source=token,)
            # Create the Payment
            payment = payment()
            payment.stripe_charge_id = charge["id"]
            payment.user = self.request.user
            payment.amount = amount
            payment.save()
            # assign the payment to the order
            order.ordered = True
            order.payment = payment
            order.save()
            messages.success(self.request, "Your order was successful")
            return redirect("core:home")

        except stripe.error.CardError as e:
            body = e.json_body
            error = body.get("error", {})
            messages.error(self.request, f"{error.get('message')}")
            return redirect("core:home")
        except stripe.error.RateLimitError as e:
            messages.error(self.request, "RateLimitError")
            return redirect("core:home")
        except stripe.error.InvalidRequestError as e:
            messages.error(self.request, "RateLimiInvalidRequestErrortError")
            return redirect("core:home")
        except stripe.error.AuthenticationError as e:
            messages.error(self.request, "AuthenticationError")
            return redirect("core:home")
        except stripe.error.APIConnectionError as e:
            messages.error(self.request, "APIConnectionError")
            return redirect("core:home")
        except stripe.error.StripeError as e:
            messages.error(self.request, "Something went wrong. Try again")
            return redirect("core:home")
        except Exception as e:
            messages.error(self.request, "A serious error occurred")
            return redirect("core:home")


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


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            content = {"object": order}
            return render(self.request, "core/order_summary.html", content)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("core:home")


@login_required
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
            return redirect("core:order-summary")
        else:
            # adding new item
            order.items.add(order_item)
            messages.info(request, "This Item was added to your cart.")
            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This Item was added to your cart.")
    return redirect("core:product", slug=slug)


@login_required
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
            return redirect("core:order-summary")
        else:
            # add a message saying the User doesnt have an Order
            messages.warning(request, "This item was not in your cart.")
            return redirect("core:product", slug=slug)

    else:
        # add a message saying the User doesnt have an Order
        messages.info(request, "You do not have an active order.")
        return redirect("core:product", slug=slug)


@login_required
def remove_count_from_cart(request, slug):
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

            if order_item.quantity == 1:
                order_item.quantity -= 1
                order.items.remove(order_item)
            elif order_item.quantity == 0:
                order.items.remove(order_item)
            else:
                order_item.quantity -= 1
            order_item.save()
            messages.warning(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            # add a message saying the User doesnt have an Order
            messages.warning(request, "This item was not in your cart.")
            return redirect("core:product")

    else:
        # add a message saying the User doesnt have an Order
        messages.info(request, "You do not have an active order.")
        return redirect("core:product")

