from tastypie.resources import ModelResource
from ferre.models import Ferreteria, Proveedor, Articulo

class FerreteriaResource(ModelResource):
	class Meta:
		queryset = Ferreteria.objects.all()
		resource_name = 'ferreteria'

class ProveedorResource(ModelResource):
	class Meta:
		queryset = Proveedor.objects.all()
        resource_name = 'proveedor'

class ArticuloResource(ModelResource):
	class Meta:
		queryset = Articulo.objects.all()
		resource_name = 'articulo'
