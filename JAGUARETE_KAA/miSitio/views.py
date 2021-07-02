from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Categoria, Producto, Carrito
# Create your views here.


def index(request):
    return render(request, "misitio/index.html")
