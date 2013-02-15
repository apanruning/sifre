from django.db import models

# Create your models here.
class Articulo(models.Model):
    cod_art = models.SlugField(null=True,blank=True)
    descripcion = models.TextField()
    marca = models.ForeignKey('Fabricante',null=True,blank=True)
    material = models.ForeignKey('Material',null=True,blank=True)
    medida = models.ForeignKey('Medida',null=True,blank=True)
    unidad = models.ForeignKey('Unidad',null=True,blank=True)
    imagen = models.ImageField(upload_to='uploads',null=True,blank=True)
    ferreteria = models.ForeignKey('Ferreteria',null=True,blank=True)
    
    def __unicode__(self):
        if self.cod_art:
            return self.cod_art + ' - ' + self.descripcion
        else:
            return "s/c" + ' - ' + self.descripcion

    class Meta:
        ordering = ('descripcion',)
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"