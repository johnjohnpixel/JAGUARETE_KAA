"""JAGUARETE_KAA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'miSitio'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('carrito/', views.carrito, name="carrito"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
    path('producto/', views.producto, name="ver_producto"),
    path('producto/<int:producto_id>/', views.producto, name="producto"),
    path('producto/añadir_producto/', views.añadir_producto, name="añadir_producto"),
    path('producto/<int:producto_id>/editar_producto/', views.editar_producto, name="editar_producto"),
    path('resultado_busqueda/', views.resultado_busqueda, name="resultado_busqueda"),
    path('borrar_producto/<int:producto_id>/', views.borrar_producto, name='borrar_producto')
]

