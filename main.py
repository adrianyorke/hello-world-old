#!/usr/bin/env python2

import os
import sys

print 'Starting this beautiful thing...'

sys.argv = ['XSDValidator.py','shiporder.xml','shiporder.xsd']
execfile('XSDValidator.py')