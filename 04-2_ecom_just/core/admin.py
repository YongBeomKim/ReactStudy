from django.contrib import admin

# Register your models here.

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address

# Django's "modeladmin" user function
# using in ADMIN page
def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


# .short_description
# message to show in admin option
make_refund_accepted.short_description = "Update orders to refund granted"


class OrderAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "ordered",
        "being_delivered",
        "received",
        "refund_requested",
        "refund_granted",
        "billing_address",
        "payment",
        "coupon",
    ]
    # in `list_display` field
    # Adding the Filtering Links
    list_display_links = [
        "user",
        "billing_address",
        "payment",
        "coupon",
    ]
    list_filter = [
        "ordered",
        "being_delivered",
        "received",
        "refund_requested",
        "refund_granted",
    ]
    search_fields = [
        "user__username",
        "ref_code",
    ]
    actions = [
        make_refund_accepted,
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "address_street",
        "address_apartment",
        # "countries", # Django: unhashable type:'list' error
        "zip_code",
        "address_type",
        "default",
    ]
    list_filter = [
        "countries",
        "address_type",
        "default",
    ]
    search_fields = [
        "user",
        "address_street",
        "address_apartment",
        "zip_code",
    ]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
