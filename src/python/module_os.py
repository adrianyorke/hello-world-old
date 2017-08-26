#!/usr/bin/env python
"""Module docstring [pylint-C0111]."""

import os

def ls(dir, hidden=False, relative=True):
    nodes = []
    for nm in os.listdir(dir):
        if not hidden and nm.startswith('.'):
            continue
        if not relative:
            nm = os.path.join(dir, nm)
        nodes.append(nm)
    nodes.sort()
    return nodes

def find(root, files=True, dirs=False, hidden=False, relative=True, topdown=True):
    root = os.path.join(root, '')  # add slash if not there
    for parent, ldirs, lfiles in os.walk(root, topdown=topdown):
        if relative:
            parent = parent[len(root):]
        if dirs and parent:
            yield os.path.join(parent, '')
        if not hidden:
            lfiles   = [nm for nm in lfiles if not nm.startswith('.')]
            ldirs[:] = [nm for nm in ldirs  if not nm.startswith('.')]  # in place
        if files:
            lfiles.sort()
            for nm in lfiles:
                nm = os.path.join(parent, nm)
                yield nm

def test(root):
    print os.getcwd()
    print "* directory listing, with hidden files:"
    print ls(root, hidden=True)
    print
    print "* recursive listing, with dirs, but no hidden files:"
    for f in find(root, dirs=True):
        print f
    print

if __name__ != "__main__":
    test(os.getcwd())
