from django import forms
from models import Proveedor, Articulo, CatalogoProveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo

class CatalogoProveedorForm(forms.ModelForm):
    class Meta:
        model = Articulo


