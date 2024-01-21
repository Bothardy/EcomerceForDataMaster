from .models import Product
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404


class IndexView(TemplateView):
    template_name = 'store/index.html'


def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


def productpage(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)
    product = Product.objects.all()

    return render(request, 'store/product.html', {'product': product})


def home(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)
    product = Product.objects.first()

    return render(request, 'store/home.html', {'product': product})


class ProductView(TemplateView):
    template_name = 'store/product.html'


def profiluser(request):
    # Fetch the first product from the database (you can modify this logic based on your needs)

    return render(request, 'store/profile.html')
