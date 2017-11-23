from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Dish, Product


# Create your views here.
def homepage(request):
    return render(request, 'base.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def shoping_list(request):
    products = Product.objects.filter(available=False)
    return render(request, 'shoping_list.html', {'products': products})
