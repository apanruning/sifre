# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from profiles.models import DefualtUserProfile
from profiles.forms import DefualtUserProfileForm
from publicaciones.models import Publicacion

@login_required
def detail(request, username):
    is_me = request.user.username == username
    try:
        user_profile = DefualtUserProfile.objects.get(user__username=username)
    except InstitucionProfile.DoesNotExist:
        if is_me:
            return redirect('profile_create', username=username)
        else:
            messages.info(request, message=u'El usuario no existe')
            return redirect('/')    
        
    return render(
        request,
        'profile.html',
        {
            'profile':user_profile,
            'is_me': is_me
        }
    )

@login_required   
def edit(request, username):
    pass

@login_required
def create(request, username):
    user = get_object_or_404(User, username=username)
    
    form = DefualtUserProfileForm(initial={'email':user.email})

    if request.method == 'POST':
        form = DefualtUserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            messages.info(request, message=u'Perfil creado')
            return redirect(profile.get_absolute_url())
            
    return render(
        request,
        'create_profile.html',
        {
            'form':form,
            'username': username,
        }
        
    )
