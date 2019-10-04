#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        result = max_integer([1, 2, 3, 4])
        self.assertIs(result, 4)
        result = max_integer([1])
        self.assertIs(result, 1)
        result = max_integer([4, 6, 3, 1])
        self.assertIs(result, 6)
        result = max_integer([])
        self.assertIs(result, None)
        result = max_integer([-90, -95, -50, -10, -5])
        self.assertIs(result, -5)
        result = max_integer([5, 5])
        self.assertIs(result, 5)
