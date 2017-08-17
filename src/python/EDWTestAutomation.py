#!/usr/bin/env python
"""Module docstring [pylint-C0111]."""

from __future__ import print_function

import sys
import os
import unittest
import re

# INFO: https://docs.python.org/2/library/unittest.html

def main():
    """this is the docstring for function main()"""
    print('main')
    print(sys.version_info)

    cwd = os.getcwd()
    print(cwd)

    os.chdir('c:\\temp')
    cwd = os.getcwd()
    print(cwd)

    #path = os.path.join("C:\\","temp")
    # rootpath = os.path.join(
    #     "C:\\"
    #     , "Temp"
    #     , "svn-temp"
    #     , "edw"
    #     , "enterprise-data-warehouse"
    #     , "trunk"
    #     , "src"
    #     , "teradata"
    #     , "DDL"
    #     , "DBADMIN"
    #     )

    #if os.path.exists(path):
    #    print(path + ' : exists')
    #    if os.path.isdir(path):
    #        print(path + ' : is a directory')

    #for root, dirs, files in os.walk(rootpath):
    #    print("{0} has {1} file(s)".format(root, len(files)))

    #files = os.listdir(rootpath)
    #for f in files:
    #    print(f)

    # fileList = []
    # for file in os.listdir(rootpath):
    #     fileList.append(file)
    # print(fileList)

    return 0

class NamingConventionsTestCase(unittest.TestCase):
    """
    def test_checkprefix(self):
        allTestsHavePassed = True

        rootpath = os.path.join(
            "C:\\"
            , "Temp"
            , "svn-temp"
            , "edw"
            , "enterprise-data-warehouse"
            , "trunk"
            , "src"
            , "teradata"
            , "DDL"
            , "DBADMIN"
            )

        for file in os.listdir(rootpath):
            if re.match(r'^D_ACQ', file, flags=0):
                pass
            elif re.match(r'^V_ACQ', file, flags=0):
                pass
            elif re.match(r'^UDF', file, flags=0):
                pass
            elif re.match(r'^V_IDL', file, flags=0):
                pass
            elif re.match(r'^D_IDL', file, flags=0):
                pass
            elif re.match(r'^D_LRY', file, flags=0):
                pass
            elif re.match(r'^V_LRY', file, flags=0):
                pass
            elif re.match(r'^ACQ_ABAS', file, flags=0):
                pass
            else:
                print(file)
                allTestsHavePassed = False

        self.assertEqual(allTestsHavePassed, True)
    """

    def test_checksuffix(self):
        allTestsHavePassed2 = True

        rootpath2 = os.path.join(
            "C:\\"
            , "Temp"
            , "svn-temp"
            , "edw"
            , "enterprise-data-warehouse"
            , "trunk"
            , "src"
            , "teradata"
            , "DDL"
            , "DBADMIN"
            )

        for file in os.listdir(rootpath2):
            if re.match(r'_STA$', file, flags=0):
                pass
            elif re.match(r'_STG$', file, flags=0):
                pass
            elif re.match(r'FSDM_BSE$', file, flags=0):
                pass
            elif re.match(r'CMMN_INM$', file, flags=0):
                pass
            elif re.match(r'N_INPUT$', file, flags=0):
                pass
            elif re.match(r'N_OUTPUT$', file, flags=0):
                pass
            else:
                print(file)
                allTestsHavePassed2 = False

        self.assertEqual(allTestsHavePassed2, True)

if __name__ == '__main__':
    unittest.main()
