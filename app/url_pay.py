from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import models

urlpatterns = [
    path('<str:final_fee>/', views.pay, name='pay'),
]