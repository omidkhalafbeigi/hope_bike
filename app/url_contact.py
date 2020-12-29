from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('send_ticket/', views.send_ticket, name='send_ticket'),
]
