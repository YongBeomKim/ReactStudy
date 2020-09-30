from django.contrib import admin
from .models import Pizza, Buger, Order, Item


# Register your models here.


class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "priceM", "priceL")


class BugerAdmin(admin.ModelAdmin):
    list_display = ("name", "priceM", "priceL")


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Buger, BugerAdmin)
admin.site.register(Order)
admin.site.register(Item)
