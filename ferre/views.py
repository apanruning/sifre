from django.shortcuts import render, redirect, get_object_or_404
from models import Proveedor, Articulo, CatalogoProveedor
from forms import ProveedorForm, CatalogoProveedorForm
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

#### INICIO PROVEEDOR ####

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

def providers_edit(request, id="1"):
    provider = Proveedor.objects.get(pk=id)
    
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=provider)        
        if form.is_valid():
            obj = form.save()
            return redirect("/providers/"+obj.pk)
    form = ProveedorForm(instance=provider) 
    
    return render(
        request,
        'proveedor_detalle.html',
        {
            'provider':provider,
            'form':form,     
            'current_time':datetime.datetime.now(),
        }
    )

def article_provider(request, id="1"):
    articles = CatalogoProveedor.objects.filter(proveedor=id).order_by('descripcion')
    provider = Proveedor.objects.get(pk=id)
    return render(
        request,
        'proveedor_ver_articulos.html',
        {
            'articles':articles,
            'current_time':datetime.datetime.now(),
            'provider':provider,
        }
    )
        

#### FIN PROVEEDOR ####

#### INICIO ARTICULO ####

def articles_manager(request):
    now = datetime.datetime.now()
    articles = Articulo.objects.all().order_by('descripcion')
    return render(
		request,
		'manager_articulos.html',
		{
        'articles':articles,
        'current_time':now,
        }
	)

def article_new_provider(request):
    if request.method == "POST":
        form = CatalogoProveedorForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("/providers/new")
    form = CatalogoProveedorForm()
    return render(
        request,
        'catalogoproveedor_nuevo.html',
        {
            'form':form,   
            'current_time':datetime.datetime.now(),  
        }
    )
    



