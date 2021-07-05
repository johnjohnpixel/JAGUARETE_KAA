from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Categoria, Producto, Carrito
from .forms import FormProductoCRUD
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

def añadir_producto(request):
    if request.method=="POST":
        form = FormProductoCRUD(request.post)
        if form.is_valid():
            form.save()
    else:
        form = FormProductoCRUD()
        return render (request, 'misitio/producto.html',{
            "formset":form
        })   

def ver_producto(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    titulo = producto.titulo
    imagen = producto.imagen
    descripcion = producto.descripcion
    precio = producto.precio 
    categoria = producto.categoria
    return render (request, 'misitio/producto.html',{
    "titulo": titulo,
    "precio": precio,
    "descripcion": descripcion,
    "imagen": imagen,
    "categoria":categoria,
    }
    )

def editar_producto(request,producto_id):
    un_producto = get_object_or_404(Producto,id=producto_id)
    if request.method=="POST":
        form= FormProductoCRUD(request.post,instance=un_producto)
        if form.is_valid():
            form.save()
            return render(request,"misitio/producto.html",{
                "Productos":Producto.objects.all(),
                "un_producto":un_producto,
            })
    else:
        form = FormProductoCRUD(instance=un_producto)
        titulo = form['titulo']
        imagen = form['imagen']
        descripcion = form['descripcion']
        precio = form['precio']
        categoria = form['categoria']
        return render(request,"misitio/producto.html",{
            "un_producto":un_producto,
            "form":form,
            "titulo": titulo,
            "precio": precio,
            "descripcion": descripcion,
            "imagen": imagen,
            "categoria":categoria,
            
        })


