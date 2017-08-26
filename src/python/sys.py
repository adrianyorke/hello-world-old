#!/usr/bin/env python
"""Module docstring [pylint-C0111]."""

import os
import sys

print 'Hello, world!'

# print dir(os)
print '---------- dir(sys)'
print dir(sys)


# print sys.__doc__

print '---------- sys.modules'
# print sys.modules
print sys.modules['heapq']

print '---------- sys.argv'
print sys.argv

print '---------- sys.path'
print sys.path

print '---------- sys.path[0]'
print sys.path[0]

print '---------- sys.version'
print sys.version
print sys.version_info

print '---------- sys.platform'
print sys.platform
