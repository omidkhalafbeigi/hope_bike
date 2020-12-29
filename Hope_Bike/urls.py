from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('sign/', include('app.url_sign')),
    path('cart/', include('app.url_cart')),
    path('accessories/', include('app.url_accessories')),
    path('bikes/', include('app.url_bikes')),
    path('about/', views.about, name='about'),
    path('contact/', include('app.url_contact')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
