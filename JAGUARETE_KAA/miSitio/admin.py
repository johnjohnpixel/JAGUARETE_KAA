from django.contrib import admin
from .models import Categoria, Producto, Carrito

# Register your models here..


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo','imagen','descripcion','precio','categoria')

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carrito)
