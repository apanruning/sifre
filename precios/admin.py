from django.contrib import admin
from precios.models import ArticuloPrecioPublico

class PrecioPublicoAdmin(admin.ModelAdmin):
    list_display = ('cod_art','descripcion','precio')
    search_fields = ("articulo__cod_art","articulo__descripcion")
    
admin.site.register(ArticuloPrecioPublico,PrecioPublicoAdmin)
