from django.contrib import admin
from stock.models import ArticuloStock

class ControlStockAdmin(admin.ModelAdmin):
    list_display = ('cod_art','descripcion','stock')
    search_fields = ("articulo__cod_art","articulo__descripcion")


admin.site.register(ArticuloStock,ControlStockAdmin)