from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

class Medida(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name = "Medida"
        verbose_name_plural = "Medidas"

class Unidad(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"

class Ferreteria(models.Model):
    cod_fer = models.SlugField()
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = "Ferreteria"
        verbose_name_plural = "Ferreterias"

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


class Fabricante(models.Model):
    cod_fab = models.SlugField('Articulo',null=True,blank=True)
    nombre = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class ArticuloStock(models.Model):
    articulo = models.ForeignKey('Articulo')
    stock = models.FloatField(default=0.0)
    
    def cod_art(self):
        return self.articulo.cod_art

    def descripcion(self):
        return self.articulo.descripcion

    class Meta:
        ordering = ('articulo__descripcion',)
        verbose_name = "Control de Stock de Articulo"
        verbose_name_plural = "Control de Stock de Articulos"
    
#este es el articulo que vende una ferreteria
class ArticuloPrecioPublico(models.Model):
    articulo = models.ForeignKey('Articulo')
    precio = models.FloatField(default=0.0)

    def cod_art(self):
        return self.articulo.cod_art

    def descripcion(self):
        return self.articulo.descripcion

    class Meta:
        ordering = ('articulo__descripcion',)
        verbose_name = "Precio de Articulo"
        verbose_name_plural = "Precios de Articulos"

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

