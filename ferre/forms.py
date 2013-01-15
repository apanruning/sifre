from django import forms
from models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor

