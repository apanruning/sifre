from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=255)

class Medida(models.Model):
    name = models.CharField(max_length=255)

class Unidad(models.Model):
    name = models.CharField(max_length=255)

class Ferreteria(models.Model):
    cod_fer = models.SlugField()
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()

class Proveedor(models.Model):
    cod_prov = models.SlugField(primary_key=True)
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()

class Fabricante(models.Model):
    cod_fab = models.SlugField('Articulo',null=True,blank=True)
    nombre = models.CharField(max_length=255)

class ArticuloStock(models.Model):
    articulo = models.ForeignKey('Articulo')
    stock = models.FloatField(default=0.0)
    
#este es el articulo que vende una ferreteria
class ArticuloPrecioPublico(models.Model):
    articulo = models.ForeignKey('Articulo')
    precio = models.FloatField(default=0.0)

class CatalogoProveedor(models.Model):
    cod_cat = models.SlugField(primary_key=True)
    articulo = models.ForeignKey('Articulo',null=True,blank=True)
    proveedor = models.ForeignKey('Proveedor',null=True,blank=True)
    descripcion = models.TextField(null=True,blank=True)
    unidad = models.ForeignKey('Unidad',null=True,blank=True)
    precio = models.FloatField(null=True,blank=True)
    fecha = models.DateField(auto_now=True, editable=False)
    
class Articulo(models.Model):
    cod_art = models.SlugField(null=True,blank=True)
    descripcion = models.TextField()
    marca = models.ForeignKey('Fabricante',null=True,blank=True)
    material = models.ForeignKey('Material',null=True,blank=True)
    medida = models.ForeignKey('Medida',null=True,blank=True)
    unidad = models.ForeignKey('Unidad',null=True,blank=True)
    imagen = models.ImageField(upload_to='uploads',null=True,blank=True)
    ferreteria = models.ForeignKey('Ferreteria',null=True,blank=True)
