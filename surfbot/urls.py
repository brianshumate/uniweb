"""
Validator project

urls.py

Created by b on 2009-06-17.
Copyright (c) 2009 Brian Shumate. All rights reserved.
"""

from django.views.generic.list_detail import object_list
from django.conf.urls.defaults import *
from surfbot.validator.models import Website

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sites_dict = {
    'queryset': Website.objects.all(),
    'paginate_by': 10,
    'template_name': 'homepage.html',
}

urlpatterns = patterns('',
    # Example:
    # (r'^surfbot/', include('surfbot.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # Custom entries begin here
    
    (r'^$', object_list, sites_dict),
    (r'^(?P<page>[0-9]+)/$', object_list, sites_dict),
)
