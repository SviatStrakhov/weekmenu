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
class ProductsListView(ListView):

    template_name = 'products.html'
    ordering = ['title']
    paginate_by = 30

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
    paginate_by = 30

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


class ProductNotesUpdateView(UpdateView):

    model = Product
    fields = ['notes']
    template_name = 'product_notes_edit.html'
    success_url = '/products'


class ShoppingProductNotesUpdateView(UpdateView):

    model = Product
    fields = ['notes']
    template_name = 'product_notes_edit.html'
    success_url = '/shopping_list'


# def test_request(request):
#     a = "<WSGIRequest: GET '/shopping_list/'>"
#     print(request)
#     if 'shopping_list' in str(request):
#         print('/shopping_list/')
#     else:
#         print('zopa')
#     return render(request, 'base.html')


class MenuView (ListView):

    template_name = 'menu.html'
    queryset = Dish.objects.all()


class DishCreate(CreateView):

    model = Dish
    fields = ['title', 'product']
    template_name = 'add_dish.html'
    success_url = '/menu'


class DishCompositionView(UpdateView):

    model = Dish
    fields = ['product']
    template_name = 'dish_composition.html'
    success_url = '/products'

