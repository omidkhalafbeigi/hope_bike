from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('exit/', views.exit, name='exit'),
]
