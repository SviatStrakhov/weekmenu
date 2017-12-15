"""weekmenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from w_menu.views import *
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView
urlpatterns = [

    url(r'^$', ShoppingListView.as_view(), name='home'),
    url(r'^shopping_list/$', ShoppingListView.as_view(), name='shopping_list'),
    url(r'^shopping_list/(?P<pk>\d+)/notes/edit$', ShoppingProductNotesUpdateView.as_view(),
        name='shopping_list_product_edit'),

    url(r'^products/$', ProductsListView.as_view(), name='products'),
    url(r'^products/(?P<pk>\d+)/notes/edit$', ProductNotesUpdateView.as_view(), name='product_notes_edit'),
    url(r'^products/add_product/$', ProductCreate.as_view(), name='add_product'),
    url(r'^products/(?P<pk>\d+)/delete_product/$', ProductDeleteView.as_view(), name='product_delete'),

    url(r'^menu/$', MenuView.as_view(), name='menu'),
    url(r'^menu/dish/add/$', DishCreate.as_view(), name='add_dish'),
    url(r'^menu/dish/(?P<pk>\d+)/edit/$', DishCompositionView.as_view(), name='dish_composition'),

    # related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')),
        name='profile'),
    url(r'^accounts/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    # url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # admin urls
    url(r'^admin/', admin.site.urls),
]
