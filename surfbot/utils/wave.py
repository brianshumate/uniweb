"""
Uniweb validator project

wave.py : Checks URL against WAVE validator in various ways

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


def checkaccess(site_pk):
    """
    Checks URL against WAVE validator website for accesibility
    FIXME: how do we internalize this?!

    """
    today = datetime.date.today()
    wave = "http://wave.webaim.org/report?url="
    w = Website.objects.get(pk=site_pk)
    w.checkok = False
    w.accessval = 'Fail'
    w.lastcheck = today
    week = timedelta(days=7)
    day = timedelta(hours=24)

    h = httplib2.Http(".cache")
    resp, content = h.request(wave + w.rooturl, "GET")
    validator = BeautifulSoup(content)
    if validator.find('h1', id='wave4errormessage'):
        w.checkok = True
        w.nextcheck = today + day
        w.checktotal += 1
        w.accessval = 'Fail'
        w.accessval_fcount += 1
        w.save()
        return w.accessval
    else:
        w.checkok = True
        w.nextcheck = today + week
        w.checktotal += 1
        w.accessval = 'Pass'
        w.accessval_pcount += 1
        w.save()
        return w.accessval