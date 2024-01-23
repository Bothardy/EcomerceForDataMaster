from .models import Product
from django.shortcuts import render, get_object_or_404




def productpage(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)
    product = Product.objects.all()

    return render(request, 'store/product.html', {'product': product})


def home(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)
    product = Product.objects.all()

    return render(request, 'store/home.html', {'product': product})


def profiluser(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)

    return render(request, 'store/profile.html')
