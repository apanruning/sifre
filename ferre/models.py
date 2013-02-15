from django.db import models
from data.models import *

class Material(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

class Medida(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = "Medida"
        verbose_name_plural = "Medidas"
    

class Unidad(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"

class Ferreteria(models.Model):
    cod_fer = models.SlugField()
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = "Ferreteria"
        verbose_name_plural = "Ferreterias"

class Fabricante(models.Model):
    cod_fab = models.SlugField(null=True,blank=True)
    nombre = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    
