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

    os.chdir(r'c:\temp')
    cwd = os.getcwd()
    print(cwd)

class DBNamingConventionsTestCase(unittest.TestCase):

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
            if re.search(r'^D_ACQ', file, flags=0):
                pass
            elif re.search(r'^V_ACQ', file, flags=0):
                pass
            elif re.search(r'^UDF', file, flags=0):
                pass
            elif re.search(r'^V_IDL', file, flags=0):
                pass
            elif re.search(r'^D_IDL', file, flags=0):
                pass
            elif re.search(r'^D_LRY', file, flags=0):
                pass
            elif re.search(r'^V_LRY', file, flags=0):
                pass
            elif re.search(r'^ACQ_ABAS', file, flags=0):
                pass
            elif re.search(r'^_GCFR_D', file, flags=0):
                pass
            elif re.search(r'^_GCFR_P', file, flags=0):
                pass
            elif re.search(r'^_GCFR_V', file, flags=0):
                pass
            elif re.search(r'^D_WRK', file, flags=0):
                pass
            else:
                print(file)
                allTestsHavePassed = False

        self.assertEqual(allTestsHavePassed, True)

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
            if re.search(r'_STA$', file, flags=0):
                pass
            elif re.search(r'_STG$', file, flags=0):
                pass
            elif re.search(r'FSDM_BSE$', file, flags=0):
                pass
            elif re.search(r'CMMN_INM$', file, flags=0):
                pass
            elif re.search(r'N_INPUT$', file, flags=0):
                pass
            elif re.search(r'N_OUTPUT$', file, flags=0):
                pass
            elif re.search(r'FSDM_N_BASE$', file, flags=0):
                pass
            elif re.search(r'UDF$', file, flags=0):
                pass
            elif re.search(r'_UTLFW$', file, flags=0):
                pass
            elif re.search(r'_CUSTOM$', file, flags=0):
                pass
            else:
                print(file)
                allTestsHavePassed2 = False

        self.assertEqual(allTestsHavePassed2, True)

if __name__ == '__main__':
    unittest.main()
