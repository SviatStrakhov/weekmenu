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
from w_menu.views import homepage, ProductsView, ShopingListView, ProductCreate
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView
urlpatterns = [

    url(r'^$', homepage, name='home'),
    url(r'^products/$', ProductsView.as_view(), name='products'),
    url(r'^shoping_list/$', ShopingListView.as_view(), name='shoping_list'),
    url(r'^products/add_product/$', ProductCreate.as_view(), name='add_product'),

    # related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),

    # admin urls
    url(r'^admin/', admin.site.urls),
]
