from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Dish, Product


# Create your views here.
def homepage(request):
    return render(request, 'base.html')


def products(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products.html', {'products': products})


def shoping_list(request):
    products = Product.objects.filter(available=False)
    return render(request, 'shoping_list.html', {'products': products})


class ProductCreate(CreateView):

    model = Product
    fields = ['title', 'available', 'notes']
    template_name = 'add_product.html'
    success_url = '/products'