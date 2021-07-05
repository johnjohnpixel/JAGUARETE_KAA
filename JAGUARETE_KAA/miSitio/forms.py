from django.forms import ModelForm
from django import forms
from .models import Producto

class FormProductoCRUD(forms.ModelForm):
    class Meta:
        model= Producto
        fields=('titulo','imagen','descripcion','precio','categoria')