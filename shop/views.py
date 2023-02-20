from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    # print("These are catprods",catprods)
    cats = {item['category'] for item in catprods}
    # print("These are categories",cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        # print("These are prods",prod)
        n = len(prod)
        # print("Length of products",n)
        nSlides = n//4 + ceil((n/4) - (n//4))
        # print("No of slides",nSlides)
        allProds.append([prod, range(1, nSlides), nSlides])
        # print(allProds)
    # params = {"no_of_slides" : nSlides, "range" : range(1, nSlides), "product" : products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        sent_name = request.POST.get('name', 'default value')
        sent_email = request.POST.get('email', 'default value')
        sent_phone = request.POST.get('phone', 'default value')
        sent_desc = request.POST.get('desc', 'default value')

        contact = Contact(name=sent_name, email=sent_email, phone=sent_phone, desc=sent_desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodView.html', {'productView':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')

