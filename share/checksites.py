#!/usr/bin/env python
# encoding: utf-8
"""
checksites.py

Created by b on 2009-06-18.
Copyright (c) 2009 Brian Shumate. All rights reserved.
"""
import os, sys
import httplib2
import urllib2
import re
from BeautifulSoup import BeautifulSoup

failed = 0
passed = 0
sitelist = "http://www.utexas.edu/world/univ/state/"
total = 0
w3chtml = "http://validator.w3.org/check?uri="
page = urllib2.urlopen(sitelist)
soup = BeautifulSoup(page)

for anchor in soup.findAll('a', href=re.compile(r'\.edu')):
    h = httplib2.Http(".cache")
    resp, content = h.request(w3chtml + anchor['href'], "GET")
    validator = BeautifulSoup(content)
    if validator.find('h3', 'invalid'):
        print anchor['href'] + ' FAIL'
        failed += 1
        total += 1
    else:
        print anchor['href'] + ' PASS'
        passed += 1
        total += 1

print 'passed: ' + passed
print 'failed: ' + failed
print 'total: ' + total