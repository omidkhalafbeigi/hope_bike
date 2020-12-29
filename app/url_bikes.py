from django.urls import path, include, re_path
from . import views


urlpatterns = [
    re_path('^$', views.bikes, name='bikes'),
    re_path(r'(?P<slug>[\w-]+)/add/$', views.add_bike_to_cart, name='add_bike_to_cart'),
    re_path(r'(?P<slug>[\w-]+)/$', views.bike_desc, name='bike_desc'),
]
