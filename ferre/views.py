from django.shortcuts import render, redirect, get_object_or_404
from models import Proveedor, Articulo
from forms import ProveedorForm
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
        form = ProveedorForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("/providers/new")
    form = ProveedorForm()
    return render(
        request,
        'proveedor_nuevo.html',
        {
            'form':form,   
            'current_time':datetime.datetime.now(),  
        }
    )

def providers_edit(request, id):
    provider = Proveedor.objects.get(pk=id)
    
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=provider)        
        if form.is_valid():
            obj = form.save()
            return redirect("/providers/"+str(obj.id))
    form = ProveedorForm(instance=provider) 
    
    return render(
        request,
        'proveedor_detalle.html',
        {
            'provider':provider.nombre,
            'form':form,     
            'current_time':datetime.datetime.now(),
        }
    )
    
