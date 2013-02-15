from django.db import models

# Create your models here.
#este es el articulo que vende una ferreteria
class ArticuloPrecioPublico(models.Model):
    articulo = models.ForeignKey('Articulo')
    precio = models.FloatField(default=0.0)

    def cod_art(self):
        return self.articulo.cod_art

    def descripcion(self):
        return self.articulo.descripcion
    
    def __unicode___(self):
        return self.articulo.__unicode() + ' - ' + self.precio

    class Meta:
        ordering = ('articulo__descripcion',)
        verbose_name = "Precio de Articulo"
        verbose_name_plural = "Precios de Articulos"

