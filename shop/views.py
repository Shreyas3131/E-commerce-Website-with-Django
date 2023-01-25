from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    params = {"no_of_slides" : nSlides, "range" : range(1, nSlides), "product" : products}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("This is Contact Page")

def tracker(request):
    return HttpResponse("This is Tracker Page")

def search(request):
    return HttpResponse("This is Search Page")

def productView(request):
    return HttpResponse("This is Product View Page")

def checkout(request):
    return HttpResponse("This is Checkout Page")

