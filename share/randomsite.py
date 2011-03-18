#!/usr/bin/env python
# encoding: utf-8
"""
Uniweb validator project

randomsite.py

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
import random
import re
import webbrowser
from BeautifulSoup import BeautifulSoup

earls = []
sitelist = "http://www.utexas.edu/world/univ/state/"

page = urllib2.urlopen(sitelist)
soup = BeautifulSoup(page)

for anchor in soup.findAll('a', href=re.compile(r'\.edu')):
    earls.append(anchor['href'])

webbrowser.open_new_tab(earls[random.randrange(0, 2038, 1)])