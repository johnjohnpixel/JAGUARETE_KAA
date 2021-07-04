from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Categoria, Producto, Carrito
# Create your views here.


def index(request):
    return render(request, "misitio/index.html")

def carrito(request):
    return render(request, "misitio/carrito.html")

def acerca_de(request):
    return render(request, "misitio/acerca_de.html")

def producto(request):
    return render(request, "misitio/producto.html")

def resultado_busqueda(request):
    return render(request, "misitio/resultado_busqueda.html")

