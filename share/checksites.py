#!/usr/bin/env python
# encoding: utf-8
"""
Uniweb validator project

checksites.py

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