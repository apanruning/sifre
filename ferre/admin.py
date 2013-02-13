'''
Created on 11/02/2013

@author: martin
'''
from django.contrib import admin
from models import *

class ProveedorAdmin(admin.ModelAdmin):
    pass

class PrecioPublicoAdmin(admin.ModelAdmin):
    list_display = ('cod_art','descripcion','precio')
    search_fields = ("articulo__cod_art","articulo__descripcion")
    
    
class ControlStockAdmin(admin.ModelAdmin):
    list_display = ('cod_art','descripcion','stock')
    search_fields = ("articulo__cod_art","articulo__descripcion")
    

class CatalogoProveedorAdmin(admin.ModelAdmin):
    
    search_fields = ("cod_cat","descripcion","proveedor__nombre","proveedor__cod_prov")

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(CatalogoProveedor, CatalogoProveedorAdmin)
admin.site.register(Articulo)
admin.site.register(ArticuloStock,ControlStockAdmin)
admin.site.register(ArticuloPrecioPublico,PrecioPublicoAdmin)
admin.site.register(Unidad)
admin.site.register(Medida)
admin.site.register(Fabricante)


