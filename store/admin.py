from django.contrib import admin
from . models import Customer, Product, ShippingAddress, Order, OrderItem

# Register your models here.
for model in [Customer, Product, ShippingAddress, Order, OrderItem]:
    admin.site.register(model)