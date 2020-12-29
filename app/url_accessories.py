from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    re_path('^$', views.accessories, name='accessories'),
    re_path(r'(?P<slug>[\w-]+)/add/$', views.add_accessories_to_cart, name='add_accessories_to_cart'),
    re_path(r'(?P<slug>[\w-]+)/$', views.accessories_desc, name='accessories_desc'),
]
