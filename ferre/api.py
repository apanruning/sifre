from tastypie.resources import ModelResource
from ferre.models import Ferreteria, Proveedor, ArticuloFerreteria

class FerreteriaResource(ModelResource):
	class Meta:
		queryset = Ferreteria.objects.all()
		resource_name = 'ferreteria'

class ProveedorResource(ModelResource):
	class Meta:
		queryset = Proveedor.objects.all()
		resource_name = 'proveedor'

class ArticuloFerreteriaResource(ModelResource):
	class Meta:
		queryset = ArticuloFerreteria.objects.all()
		resource_name = 'articulo_de_ferreteria'
