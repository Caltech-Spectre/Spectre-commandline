#!/usr/bin/python

# Spectre batch addition script

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

import amazon, spectre, readline, time

print "Spectre Mass Cataloging script"
print "Please be advised, this script is designed to be fast when adding many"
print "books at once; if you want to edit a book already in the db or to add"
print "just a single book or use a pretty interface use the webapp. If not sure"
print "how, ask Alex."
print ""

while 1:
  barcode = raw_input("Next book. Please scan the barcode now: ")
  while len(spectre.print_dupes(barcode)) > 0 or barcode == "":
    if barcode == "":
      print "I can't let you do that Dave."
    else:
      print "That barcode is already in use."
    barcode = raw_input("Please scan the barcode now: ")

  isbn = None
  while isbn == None:
    isbn = raw_input("Please enter the ISBN: ")
    arec = []
    if isbn == "":
      isbn = "0"
    elif isbn[-1] == "!":
      isbn = isbn[:-1]
    else:
      try:
        arec = amazon.lookup(isbn)
      except:
        print "An error occured. Typo? Just hit ENTER for books with no ISBN."
	print "Enter the isbn with a ! at the end to force acceptance."
        isbn = None
        continue

  trec = {"title":"", "author":"", "isbn":isbn,"idcode":barcode}

  if len(arec) > 0:
    amazon.display(arec)
    if len(arec) > 1:
      n = raw_input("Select the closest match: ")
      r = arec[int(n)]
    else:
      r = arec[0]
    authors = ""
    if 'Authors' in r:
      for i in r['Authors']:
        authors += i.split()[-1] + ", " + ' '.join(i.split()[:-1]) + " and "
      authors = authors[:-5]
    a = time.localtime()
    trec = {"title":r['ProductName'], "author":authors, "isbn":isbn, "idcode":barcode, "bought":"%i-%i-%i" % (a[0], a[1], a[2]), "checkouts":"0"}

  print "\nCorrections can now be made. Type first a single lowercase letter"
  print "t, a, i, b for title, author, isbn, barcode, then (with no space) the"
  print "new value. For example, you could type:"
  print "tHyperion<ENTER>\n\n"


  cmd = " "
  while cmd != "":
    for i in trec:
      print "%s: %s" % (i, trec[i])
    print "\n"

    cmd = raw_input("<3>> ")
    if len(cmd) > 0:
      if cmd[0] in ('t', 'a', 'i', 'b'):
        if cmd[0] == 't':
          trec['title'] = cmd[1:]
        if cmd[0] == 'a':
          trec['author'] = cmd[1:]
        if cmd[0] == 'i':
          trec['isbn'] = cmd[1:]
        if cmd[0] == 'b':
          trec['idcode'] = cmd[1:]
      else:
        print "Invalid command. use t, a, i, or b"

  spectre.addbook(trec)
  print "Book added."
