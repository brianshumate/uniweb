"""
Validator project

models.py

Created by b on 2009-06-17.
Copyright (c) 2009 Brian Shumate. All rights reserved.
"""
from datetime import datetime

from django.db import models
from django.contrib import admin
from django.conf import settings

class Website (models.Model):
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    org = models.CharField(max_length=128)
    rooturl = models.CharField(max_length=4096, help_text='Enter URL in the form of: http://www.example.com/')
    checkok = models.BooleanField()
    htmlval = models.CharField(max_length=5, blank=True)
    htmlval_fcount = models.IntegerField()
    htmlval_pcount = models.IntegerField()
    cssval = models.CharField(max_length=5, blank=True)
    cssval_fcount = models.IntegerField()
    cssval_pcount = models.IntegerField()
    accessval = models.CharField(max_length=5, blank=True)
    accessval_fcount = models.IntegerField()
    accessval_pcount = models.IntegerField()
    linksval = models.CharField(max_length=5, blank=True)
    linksval_fcount = models.IntegerField()
    linksval_pcount = models.IntegerField()
    lastcheck = models.DateField()
    nextcheck = models.DateField()
    checktotal = models.IntegerField(blank=True)
    """This is the model for target website to be checked out"""
    def __unicode__(self):
        return self.org

    def save(self, force_insert=False, force_update=False):
        if not self.pk:
            self.created = datetime.now()
            self.modified = datetime.now()
            self.htmlval_fcount = 0
            self.htmlval_pcount = 0
            self.cssval_fcount = 0
            self.cssval_pcount = 0
            self.accessval_fcount = 0
            self.accessval_pcount = 0
            self.linksval_fcount = 0
            self.linksval_pcount = 0
        else:
            self.modified = datetime.now()
        super(Website, self).save(force_insert=force_insert, force_update=force_update)