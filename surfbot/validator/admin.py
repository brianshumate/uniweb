"""
Validator project

admin.py

Created by b on 2009-06-17.
Copyright (c) 2009 Brian Shumate. All rights reserved.
"""

from surfbot.validator.models import Website
from django.contrib import admin

class WebsiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['org']}),
        (None, {'fields': ['rooturl']}),
        # ('Validation', {'fields': ['checkok', 'htmlval', 'cssval', 'accessval', 'linksval'], 'classes': ['collapse']}),
        ('Validation', {'fields': ['checkok', 'htmlval', 'cssval', 'accessval', 'linksval']}),
        ('Metrics', {'fields': ['lastcheck', 'nextcheck','checktotal']}),
    ]
        
admin.site.register(Website, WebsiteAdmin)