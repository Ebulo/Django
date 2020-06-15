from django.shortcuts import render
from django.http import HttpResponse
from .models import product, Contact
from math import ceil


def index(request):
    # products = product.objects.all()
    # n = len(products)
    # NSlides = n//4 + ceil(n/4 - n//4)
    # allprods = [[products, range(1, NSlides), NSlides],
                # [products, range(1, NSlides), NSlides]]
    # params = {'allprods': allprods}
    # params = {'no_of_slides': NSlides, 'range': range(1, NSlides), 'product': products}


    allprods = []
    a = product.objects.values('category', 'id')
    b = {item['category'] for item in a}
    for i in b:
        prod = product.objects.filter(category=i)
        n = len(prod)
        NSlides = n//6 + ceil(n/6 - n//6)
        allprods.append([prod, range(1, NSlides), NSlides])

    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)


def about(request):

    params1 = {}
    return render(request, 'shop/about.html')


def contact(request):
    name = request.POST.get('name', '')
    Email = request.POST.get('Email', '')
    phone = request.POST.get('phone', '')
    desc = request.POST.get('desc', '')
    contact = Contact(name=name, Email=Email, phone=phone, desc=desc)
    contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productview(request, myid):
    # Fetch the id
    Product = product.objects.filter(id=myid)
    print(Product)
    return render(request, 'shop/productview.html', {'product': Product[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')
