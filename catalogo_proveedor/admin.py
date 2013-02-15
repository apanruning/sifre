from models import Proveedor, CatalogoProveedor
from django.contrib import admin


class ProveedorAdmin(admin.ModelAdmin):
    pass


class CatalogoProveedorAdmin(admin.ModelAdmin):
    
    search_fields = ("cod_cat","descripcion","proveedor__nombre","proveedor__cod_prov")

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(CatalogoProveedor, CatalogoProveedorAdmin)
