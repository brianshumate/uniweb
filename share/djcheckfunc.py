#!/usr/bin/env python
# encoding: utf-8
"""
Uniweb validator project

djcheckfunc.py

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