from django.db import models

# Create your models here.
class ArticuloStock(models.Model):
    articulo = models.ForeignKey('Articulo')
    stock = models.FloatField(default=0.0)
    
    def cod_art(self):
        return self.articulo.cod_art

    def descripcion(self):
        return self.articulo.descripcion
    
    def __unicode___(self):
        return self.articulo.__unicode() + ' - ' + self.stock

    class Meta:
        ordering = ('articulo__descripcion',)
        verbose_name = "Control de Stock de Articulo"
        verbose_name_plural = "Control de Stock de Articulos"
