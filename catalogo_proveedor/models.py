from django.db import models

# Create your models here.
class Proveedor(models.Model):
    cod_prov = models.SlugField(primary_key=True)
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.cod_prov + ' - ' + self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        
class CatalogoProveedor(models.Model):
    cod_cat = models.SlugField(primary_key=True)
    articulo = models.ForeignKey('Articulo',null=True,blank=True)
    proveedor = models.ForeignKey('Proveedor',null=True,blank=True)
    descripcion = models.TextField(null=True,blank=True)
    unidad = models.ForeignKey('Unidad',null=True,blank=True)
    precio = models.FloatField(null=True,blank=True)
    fecha = models.DateField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.proveedor.nombre + ' - ' + self.cod_cat + ' - ' + self.descripcion 

    class Meta:
        ordering = ('descripcion',)
        verbose_name = "Catalogo de Proveedor"
        verbose_name_plural = "Catalogos de Proveedores"