from django.db import models

class Articulo (models.Model):
	cod_art = models.SlugField()
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='uploads')

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
	precio = models.FloatField()
	stock = models.SmallIntegerField(default=0)

class CatalogoProveedor (models.Model):
	cod_cat = models.SlugField()
	articulo = models.ForeignKey('Articulo')
	proveedor = models.ForeignKey('Proveedor')
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='uploads')
	precio = models.FloatField()
	fabricante = models.ForeignKey('Fabricante')

