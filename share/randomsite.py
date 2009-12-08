#!/usr/bin/env python
# encoding: utf-8
"""
Uniweb validator project

randomsite.py

Created by Brian Shumate on 2009-06-17.
Copyright (c) 2009 Brian Shumate. All rights reserved.
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
