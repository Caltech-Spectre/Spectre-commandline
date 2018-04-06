#!/usr/bin/python

# Spectre SQLite interface library

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

from pysqlite2 import dbapi2 as sqlite

spectre = sqlite.connect("spectre.sql")

def lookup_isbn(data):
  query = spectre.execute("select * from Books where isbn = \"%s\";" % data)
  qd = query.description
  rval = []
  fa = query.fetchall()
  for rec in fa:
    rcur = {}
    for i in range(len(qd)):
      rcur[qd[i][0]] = rec[i]
    rval.append(rcur)
  return rval

def lookup(data):
  query = spectre.execute("select * from Books where idcode = \"%s\";" % data)
  qd = query.description
  rval = []
  fa = query.fetchall()
  for rec in fa:
    rcur = {}
    for i in range(len(qd)):
      rcur[qd[i][0]] = rec[i]
    rval.append(rcur)
  return rval

def addbook(data):
  qs = "insert into Books ("
  for i in data:
    qs += "\"%s\"," % i
  qs = qs[:-1] + ") values ("
  for i in data:
    s = ''
    for c in data[i]:
      if c == '"':
        s += "''"
      else:
        s += c
    qs += "\"%s\"," % s
  qs = qs[:-1] + ");"
  result = spectre.execute(qs)
  spectre.commit()

def print_dupes(data):
  res = lookup(data)
  if len(res) > 0:
    print "Duplicates:"
    for i in res:
      print "\t", i['title'], "/", i['author'], "/", i['isbn']
  elif data != "":
    print "Barcode accepted."
  return res
