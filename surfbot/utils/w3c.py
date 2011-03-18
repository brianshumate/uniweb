"""
Uniweb validator project

w3c.py : Checks URL against W3C validators in various ways

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

import datetime
import httplib2
import urllib2
from datetime import timedelta
from BeautifulSoup import BeautifulSoup
from surfbot.validator.models import Website


def checkhtml(site_pk):
    """
    Checks URL against W3C HTML validator website
    Eventually, this will be pointed directly at a local instance as
    part of the whole appliance idea.

    """
    today = datetime.date.today()
    w3chtml = "http://validator.w3.org/check?uri="
    w = Website.objects.get(pk=site_pk)
    w.checkok = False
    w.htmlval = 'Fail'
    w.lastcheck = today
    week = timedelta(days=7)
    day = timedelta(hours=24)

    h = httplib2.Http(".cache")
    resp, content = h.request(w3chtml + w.rooturl, "GET")
    validator = BeautifulSoup(content)
    if validator.find('h3', 'invalid'):
        w.checkok = True
        w.nextcheck = today + day
        w.checktotal += 1
        w.htmlval = 'Fail'
        w.htmlval_fcount += 1
        w.save()
        return w.htmlval
    else:
        w.checkok = True
        w.nextcheck = today + week
        w.checktotal += 1
        w.htmlval = 'Pass'
        w.htmlval_pcount += 1
        w.save()
        return w.htmlval


def checkcss(site_pk):
    """
    Checks URL against W3C CSS validator website

    """
    today = datetime.date.today()
    w3ccss = "http://jigsaw.w3.org/css-validator/validator?uri="
    w = Website.objects.get(pk=site_pk)
    w.checkok = False
    w.cssval = 'Fail'
    w.lastcheck = today
    week = timedelta(days=7)
    day = timedelta(hours=24)

    h = httplib2.Http(".cache")
    resp, content = h.request(w3ccss + w.rooturl, "GET")
    validator = BeautifulSoup(content)
    if validator.find('div', id='errors'):
        w.checkok = True
        w.nextcheck = today + day
        w.checktotal += 1
        w.cssval = 'Fail'
        w.cssval_fcount += 1
        w.save()
        return w.cssval
    else:
        w.checkok = True
        w.nextcheck = today + week
        w.checktotal += 1
        w.cssval = 'Pass'
        w.cssval_pcount += 1
        w.save()
        return w.cssval