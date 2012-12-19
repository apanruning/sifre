# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.contrib import admin
from tastypie.api import Api
from ferre import api
from ferre.api import FerreteriaResource, ArticuloFerreteriaResource, ProveedorResource


api = Api(api_name = 'v1')
api.register(ProveedorResource())

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ferre.views.home', name='home'),
)

urlpatterns += patterns('',
    url(r'^api/', include(api.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^login$', 'login', {'template_name':'login.html'}, 'login'),
    (r'^logout$', 'logout', {'next_page':'/'}, 'logout'),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
