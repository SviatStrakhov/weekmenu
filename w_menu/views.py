from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Dish, Product


# Create your views here.
@login_required
def homepage(request):
    return render(request, 'base.html')


class ProductsView(ListView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductsView, self).dispatch(*args, **kwargs)

    template_name = 'products.html'
    try:
        queryset = Product.objects.filter(available=True)
    except ObjectDoesNotExist:
        pass

# def products(request):
#     products = Product.objects.filter(available=True)
#     return render(request, 'products.html', {'products': products})

class ShopingListView(ListView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShopingListView, self).dispatch(*args, **kwargs)

    template_name = 'shoping_list.html'
    queryset = Product.objects.filter(available=False)

    def get_context_data(self, **kwargs):
        context = super(ShopingListView, self).get_context_data(**kwargs)
        update_url = reverse('shoping_list')
        products = []
        # products.append({
        #     'product': product.title,
        #     'id': product.id,
        #     'update_url': update_url,
        # })
        return context

    def post(self, request, *args, **kwargs):
        return JsonResponse({'key': 'value'})


class ProductCreate(CreateView):

    model = Product
    fields = ['title', 'available', 'notes']
    template_name = 'add_product.html'
    success_url = '/products'