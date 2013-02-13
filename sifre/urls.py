# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.contrib import admin
from tastypie.api import Api
from ferre import api
from ferre.api import FerreteriaResource, ArticuloResource, ProveedorResource


api = Api(api_name = 'api_rest')
api.register(ProveedorResource())

admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^$', 'ferre.views.home', name='home'),

    #### PROVEEDORES ####
#    url(r'^providers/manager', 'ferre.views.providers_manager'),
#    url(r'^providers/new', 'ferre.views.providers_new'),
#    url(r'^providers/(?P<id>\w+)/$', 'ferre.views.providers_edit'),
#    url(r'^providers/(?P<id>\w+)/articles/$', 'ferre.views.article_provider'),
#    url(r'^providers/articles/new/$', 'ferre.views.article_new_provider'),
    #### FIN PROVEEDORES ####

    #### ARTICULO ####
#    url(r'^articles/manager', 'ferre.views.articles_manager'),
    #url(r'^articles/new', 'ferre.views.articles_new'),
    #url(r'^articles/(?P<id>\d+)/$', 'ferre.views.articles_edit'),
    #### FIN ARTICULO ####
)

#urlpatterns += patterns('',
#    url(r'^api/', include(api.urls)),
#)

#urlpatterns += patterns('django.contrib.auth.views',
#    (r'^login$', 'login', {'template_name':'login.html'}, 'login'),
#    (r'^logout$', 'logout', {'next_page':'/'}, 'logout'),
#)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
