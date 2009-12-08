#!/usr/bin/env python
# encoding: utf-8
"""
Uniweb validator project

checkfunc.py

Created by Brian Shumate on 2009-06-17.
Copyright (c) 2009 Brian Shumate. All rights reserved.
"""
import os, sys
import httplib2
import urllib2
import re
from BeautifulSoup import BeautifulSoup
from surfbot.validator.models import Website

w = Website
earl = sys.argv[1]
w3chtml = "http://validator.w3.org/check?uri="

def htmlval(url):
    h = httplib2.Http(".cache")
    resp, content = h.request(w3chtml + url, "GET")
    validator = BeautifulSoup(content)
    if validator.find('h3', 'invalid'):
        return False
    else:
        return True

if htmlval(earl):
    print 'that shit is valid yo'
else:
    print 'that is not valid'