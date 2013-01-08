from django.shortcuts import render, redirect, get_object_or_404
from models import Proveedor, Articulo
from forms import ProveedorNuevoForm
import datetime

def home(request):
    now = datetime.datetime.now()
    articles = Articulo.objects.all().order_by('descripcion')

    return render(
		request,
		'index.html',
        {
        'current_time':now,
        'articles':articles,
        }
	)

def providers_manager(request):
    now = datetime.datetime.now()
    providers = Proveedor.objects.all().order_by('nombre')
    return render(
		request,
		'manager_proveedor.html',
		{
        'providers':providers,
        'current_time':now,
        }
	)

def providers_new(request):
    if request.method == "POST":
        form = ProveedorNuevoForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("/providers/new")
    form = ProveedorNuevoForm()
    return render(
        request,
        'proveedor_nuevo.html',
        {
            'form':form,     
        }
    )

def providers_edit(request, id):
    provider = Proveedor.objects.get(pk=id)
    form = ProveedorNuevoForm(instance=provider)
    import pdb; pdb.set_trace()
    if form.is_valid():
        form.save()
    return render(
        request,
        'proveedor_detalle.html',
        {
            'form':form,     
        }
    )
    
