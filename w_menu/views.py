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

    model = Product
    template_name = 'products.html'
    ordering = ['title']
    paginate_by = 3

    try:
        queryset = Product.objects.filter(available=True)
    except ObjectDoesNotExist:
        pass


@method_decorator(login_required, name='dispatch')
class ShoppingListView(ListView):

    template_name = 'shopping_list.html'
    ordering = ['title']
    paginate_by = 3
    queryset = Product.objects.filter(available=False)


    def get_context_data(self, **kwargs):
        context = super(ShoppingListView, self).get_context_data(**kwargs)
        # update_url = reverse('shopping_list')
        # products.append({
        #     'product': product.title,
        #     'id': product.id,
        #     'update_url': update_url,
        # })
        # context['update_url'] = update_url
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        available = data['available'] and True or False
        product = Product.objects.get(pk=data['pik'])
        product.available = available
        product.save()

        return JsonResponse({'status': 'success'})


class ProductCreate(CreateView):

    model = Product
    fields = ['title', 'available', 'notes']
    template_name = 'add_product.html'
    success_url = '/products'
