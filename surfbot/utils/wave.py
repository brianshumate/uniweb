"""
wave.py : Checks URL against WAVE validator in various ways

Created by Brian Shumate on 2009-06-18.
Copyright (c) 2009 Brian Shumate. All rights reserved.

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