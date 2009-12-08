#!/usr/bin/env python
# encoding: utf-8
"""
djcheckfunc.py

Created by Brian Shumate on 2009-06-18.
Copyright (c) 2009 Brian Shumate. All rights reserved.
"""
import os, sys
import datetime
import httplib2
import urllib2
import re
from BeautifulSoup import BeautifulSoup
from surfbot.validator.models import Website

site = sys.argv[1]
w = Website.objects.get(pk=site)

w3chtml = "http://validator.w3.org/check?uri="
w.checkok = False
w.htmlval = False
w.cssval = False
w.sect508val = False
w.wcag1val = False
w.linksval = False
w.lastcheck = datetime.date.today()

def htmlval(url):
    h = httplib2.Http(".cache")
    resp, content = h.request(w3chtml + w.rooturl, "GET")
    validator = BeautifulSoup(content)
    if validator.find('h3', 'invalid'):
        w.checkok = True
        w.nextcheck = datetime.date.timedelta(days=1)
        w.checktotal =+ 1
        return False
    else:
        w.checkok = True
        w.nextcheck = datetime.date.timedelta(weeks=1)
        w.checktotal =+ 1
        return True
      
if htmlval(site):
    w.htmlval = True
    print 'that shit is valid yo'
else:
    w.htmlval = False
    print 'that is not valid'