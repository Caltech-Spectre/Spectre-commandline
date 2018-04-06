#!/usr/bin/python

# Spectre amazon.com interface library

# Copyright (C) 2008
# Alex Roper
# alexr@ugcs.caltech.edu
# S. P. E. C. T. R. E Speculative Fiction Library
# California Institute of Technology

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import SOAPpy, pickle

url = 'http://soap.amazon.com/schemas3/AmazonWebServices.wsdl'
proxy = SOAPpy.WSDL.Proxy(url)

def lookup(isbn):
  request = { 'keyword': isbn,
              'page':     '1', 
              'mode':     'books', 
              'tag':      '', 
              'type':     'heavy', 
              'devtag':   '1CQXRZP4AFE6S6CE6NR2' }

  res = proxy.KeywordSearchRequest(request)[2]
  try:
    pickle.dump(res, open("amazoncache/" + isbn, 'w'))
  except:
    pass

  rval = []
  for i in res:
    if i['Catalog'] == "Book":
      rval.append(i._asdict())
  return rval

def display(objs):
  for i in range(len(objs)):
    print "(%i)" % i
    display_single(objs[i])
    print ""

def display_single(obj):
  print "ISBN: ", obj["Asin"]
  print "Title: ", obj["ProductName"]

  if 'Authors' in obj:
    a = obj['Authors']
    if len(a) == 1:
      print "Author: ", a[0]
    else:
      print "Authors: ", a[0],
      for i in a[1:]:
        print ",", i,
      print "",
