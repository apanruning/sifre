from django.db import models

class Articulo (models.Model):
    cod_art = models.SlugField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='uploads')
    marca = models.ForeignKey('Fabricante',null=True,blank=True)
    material = models.ForeignKey('Material',null=True,blank=True)
    medida = models.ForeignKey('Medida',null=True,blank=True)

class Material(models.Model):
    name = models.CharField(max_length=255)

class Medida(models.Model):
    name = models.CharField(max_length=255)

class Ferreteria (models.Model):
    cod_fer = models.SlugField()
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()

class Proveedor (models.Model):
    cod_prov = models.SlugField()
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()

class Fabricante (models.Model):
    cod_fab = models.SlugField()
    nombre = models.CharField(max_length=255)

class ArticuloFerreteria (models.Model):
    articulo = models.ForeignKey('Articulo')
    ferreteria = models.ForeignKey('Ferreteria')
    stock = models.SmallIntegerField(default=0)
    proveedor = models.ManyToManyField('Proveedor')

#este es el articulo que vende una ferreteria
class ArticuloFerreteriaPublico(models.Model):
    art_ferre = models.ForeignKey('ArticuloFerreteria')
    precio = models.FloatField()
    unidad = models.ForeignKey('Unidad',null=True,blank=True)

class CatalogoProveedor(models.Model):
    cod_cat = models.SlugField()
    articulo = models.ForeignKey('Articulo',null=True,blank=True)
    proveedor = models.ForeignKey('Proveedor')
    descripcion = models.TextField()
    unidad = models.ForeignKey('Unidad',null=True,blank=True)
    precio = models.FloatField()
    fecha = models.DateField(auto_now=True, editable=False)
    

class Unidad(models.Model):
    name = models.CharField(max_length=255)
    

