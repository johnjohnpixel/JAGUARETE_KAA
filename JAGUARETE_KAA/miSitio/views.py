from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Categoria, Producto, Carrito
from .forms import FormProductoCRUD
# Create your views here.


def index(request):
    productos = Producto.objects.all()
    categoriax = Categoria.objects.all()
    return render(request, "misitio/index.html",{
        "productos": productos,
        "categoriax": categoriax,
    })

def carrito(request):
    lista = Carrito.lista_productos
    return render(request, "misitio/carrito.html",{
        "lista" : lista,
    })
    

lista_productos = []

@login_required
def añadir_a_carrito(request,producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito,created = Carrito.objects.get_or_create(user=request.user, active=True)
    Carrito.añadir_a_carrito(producto_id)
    return render(request, 'misitio/carrito.html')
    


def acerca_de(request):
    return render(request, "misitio/acerca_de.html")

def producto(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    titulo = producto.titulo
    imagen = producto.imagen
    descripcion = producto.descripcion
    precio = producto.precio 
    categoria = producto.categoria
    return render(request, 'misitio/producto.html',{
    "producto" : producto,
    "files":Producto.objects.all(),
    "titulo": titulo,
    "precio": precio,
    "descripcion": descripcion,
    "imagen": imagen,
    "categoria":categoria,
    "producto_id":producto_id
    }
    )

def resultado_busqueda(request):
    productos = Producto.objects.all()
    query = request.GET.get("q")
    if query and query != '':
        productos = Producto.objects.filter(Q(titulo__icontains=query) | Q(categoria__descripcion__icontains=query)) 
    else:
        productos = Producto.objects.all()
    return render(request, "misitio/resultado_busqueda.html",{
        "productos": productos,
    })

@login_required
def añadir_producto(request):
    if request.method=="POST":
        form = FormProductoCRUD(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FormProductoCRUD()
    return render(request, 'misitio/añadir_producto.html',{
            "formset":form,
            "files":Producto.objects.all(),
        })   

@login_required
def editar_producto(request,producto_id):
    un_producto = get_object_or_404(Producto,id=producto_id)
    if request.method=="POST":
        form= FormProductoCRUD(request.POST, request.FILES,instance=un_producto)
        if form.is_valid():
            form.save()
            return render(request,"misitio/editar_producto.html",{
                "Productos":Producto.objects.all(),
                "un_producto":un_producto,
            })
    else:
        form = FormProductoCRUD(instance=un_producto)
        return render(request,"misitio/editar_producto.html",{
            "un_producto":un_producto,
            "formset":form,
        })

def borrar_producto(request,producto_id):
    un_producto=get_object_or_404(Producto, id = producto_id)
    if request.method == 'POST':        
        un_producto.delete()                     

    return render(request, 'index.html', {'un_producto': un_producto})