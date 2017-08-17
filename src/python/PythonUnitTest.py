#!/usr/bin/env python
"""Module docstring [pylint-C0111]."""

from __future__ import print_function

import sys
import unittest

class TestStringMethods(unittest.TestCase):

    def test_always_pass(self):
        """Test Case: Always Pass"""
        pass

    @unittest.skip("demonstrating skipping - failure is ignored")
    def test_always_fail(self):
        """Test Case: Always Fail"""
        self.fail('This is supposed to always fail!')

    def test_upper(self):
        """Test Case: upper()"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Test Case: isupper()"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """Test Case: split()"""
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    print(sys.version_info)
    unittest.main()
