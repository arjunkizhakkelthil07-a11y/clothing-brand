from django.shortcuts import render, redirect
from .models import Product

def home(request):
    products = Product.objects.all()[:3]
    return render(request, 'home.html', {'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})

def collection(request):
    products = Product.objects.all()
    return render(request, 'collection.html', {'products': products})