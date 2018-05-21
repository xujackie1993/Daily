#!/usr/bin/env python
# -*- coding: utf-8 -*-
def TestOpionparser():
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option("-r", "--recalculate",
                    dest="recalculate",
                    default='n',
                    help="To recalculate or not. If you wants do it, must be 'y'")
  parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
  parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
  (options, args) = parser.parse_args()
  print (options.filename)
  print (options.verbose)
  print (args)