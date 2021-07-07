from .models import Categoria
from django.utils.html import escape, strip_tags

def add_variable_to_context(request):
    categorias = Categoria.objects.select_related().all().values_list('descripcion')
    categoria = Categoria.descripcion
    return {
        "categorias": categorias,
        "categoria": categoria
    }