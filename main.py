#!/usr/bin/env python2

import os
import sys

# INFO: Sample files - https://www.w3schools.com/xml/schema_example.asp
# INFO: https://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files
# INFO: https://stackoverflow.com/questions/5788891/execute-a-file-with-arguments-in-python-shell

# Modified XSD file to make it fail: renamed element title to title_fail

print 'Starting this beautiful thing...'

sys.argv = ['XSDValidator.py','shiporder.xml','shiporder.xsd']
execfile('XSDValidator.py')