from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Dish, Product


@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):

    template_name = 'base.html'


@method_decorator(login_required, name='dispatch')
class ProductsView(ListView):

    template_name = 'products.html'
    ordering = ['title']
    paginate_by = 15

    try:
        queryset = Product.objects.filter(available=True)
    except ObjectDoesNotExist:
        pass

    def post(self, request, *args, **kwargs):
        data = request.POST
        product = Product.objects.get(pk=data['pk'])
        product.available = False
        product.save()

        return JsonResponse({'status': 'success'})


@method_decorator(login_required, name='dispatch')
class ShoppingListView(ListView):

    template_name = 'shopping_list.html'
    ordering = ['title']
    paginate_by = 15

    try:
        queryset = Product.objects.filter(available=False)
    except ObjectDoesNotExist:
        pass

    def post(self, request, *args, **kwargs):
        data = request.POST
        product = Product.objects.get(pk=data['pk'])
        available = False if product.available else True
        product.available = available
        product.save()

        return JsonResponse({'status': 'success'})


class ProductCreate(CreateView):

    model = Product
    fields = ['title', 'available', 'notes']
    template_name = 'add_product.html'
    success_url = '/products'
