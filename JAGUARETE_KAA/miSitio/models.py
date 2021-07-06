from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Categoria(models.Model):
    descripcion = models.CharField(max_length=180)

    def __str__(self):
        return f"Categoria #{self.id}: {self.descripcion}."


class Producto(models.Model):
    titulo = models.CharField(max_length=64)
    imagen = models.ImageField(upload_to='')
    descripcion = models.CharField(max_length=180)
    precio = models.DecimalField(max_digits=64, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="categoria")

    def __str__(self):
        return f'El Producto #{self.id}, {self.titulo}, se describe como {self.descripcion}, pertenece a la categoria {self.categoria} y tiene un precio de ${self.precio}.'


class Carrito(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="usuario")
    lista_productos = models.ManyToManyField(
        Producto, blank=True, related_name="productos")
    total_carrito = models.DecimalField(max_digits=64, decimal_places=2)

    def __str__(self):
        return f"El Usuario {self.usuario}, posee un carrito con los productos: {self.lista_productos}, con un monto total de ${self.total_carrito}."
