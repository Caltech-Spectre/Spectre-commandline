#!/usr/bin/python

# Simple search script

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

import spectre, readline

while 1:
  barcode = raw_input("Please scan the barcode now: ")
  res = spectre.lookup(barcode)
  if len(res) > 0:
    for i in res:
      print i['title'], "/", i['author'], "/", i['isbn']
