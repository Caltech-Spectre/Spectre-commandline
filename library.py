#!/usr/bin/python

# Spectre batch addition script

# Copyright (C) 2008
# Alex Roper
# alexr@ugcs.caltech.edu
# S. P. E. C. T. R. E Speculative Fiction Library
# California Institute of Technology

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or 3 as
# published by the Free Software Foundation

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import spectre

def menu():
  print """
Welcome to S. P. E. C. T. R. E"
Should the computer fail you, sign books in and out using the green book on
the computer desk. Hold Ctrl and hit C to return to this menu at any time.

1) Check out
2) Return
3) Create account
"""
  return commands.get(raw_input("Choose> "), lambda: None)

def checkout():
  print "Scan the books one at a time. If a book does not have a barcode" \
        " enter its name as you would in a paper log. When all books are" \
        " scanned, hit enter at the prompt to continue. To remove a book" \
        " already entered, enter the number to the left of it."
  a = []
  while 1:
    print "Del Index\tTitle/Author"
    for i in range(len(a)):
      print "%i\t\t%s" % (-i - 1, a[i][1])

    v = raw_input("Scan> ")

    if v == "":
      break

    # Case: delete item
    ind = False
    try:
      ind = int(v)
      if -ind - 1 in range(len(a)):
        del a[-ind - 1]
        continue
    except ValueError: pass

    if ind and ind >= 0:
      r = spectre.lookup(v)
      
      # Case: one instance in catalog
      if len(r) == 1:
        a.append((r, "%s / %s" % (r[0]["title"], r[0]["author"])))

      # Case: not found or multiple found enter text plzkthx
      elif len(r) != 1 and ind and ind >= 0:
        print "Something's wrong; we can't find the book or we have multiple" \
              " books with that barcode. Just enter the " \
              " title and we'll fix the problem later:-)"
        continue
        
    # Case: user entered description
    elif not ind:
      a.append((None, v))

  # Do the checkout part
  print "\nPlease enter your UID or swipe your ID card in the reader." \
        " If you want to create an account now, just hit enter."

  id = raw_input("UID> ")
  if not id:
    id = newacct()

  c = ""
  while c not in "12":
    print "OK to check out these books to UID %i (%s <%s>)?\n" \
          "1) Yes\n2) No"
    c = raw_input("Choice> ")

  if c == "1":
    print "UNIMPLEMENTED"

  elif c == "2":
    return

def checkin():
  pass

def newacct():
  return 1605773

commands = {'1':checkout, '2':checkin, '3':newacct}

def main():
  while 1:
    cmd = menu()
    try: cmd()
    except KeyboardInterrupt: pass

if __name__ == "__main__": main()
