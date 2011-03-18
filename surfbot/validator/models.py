"""
Uniweb validator project

models.py

Copyright (c) 2009 Brian Shumate

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

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