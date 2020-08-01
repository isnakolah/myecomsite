from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Product, OrderItem, Order, ShippingAddress
from django.views import generic

# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/index.html', context)

def view_cart(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/index.html', context)