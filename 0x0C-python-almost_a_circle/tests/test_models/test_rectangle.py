#!/usr/bin/python3

"""
Unittesting for class Rectangle
"""

import unittest
import sys
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    #width height x y id constructor
    def test1_inputs_correct(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

    def test2_inputs_correct(self):
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r2), "[Rectangle] (1) 3/4 - 1/2")

    def test3_inputs_correct(self):
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(str(r3), "[Rectangle] (2) 3/0 - 1/2")

    def test4_inputs_correct(self):
        r4 = Rectangle(1, 2)
        self.assertEqual(str(r4), "[Rectangle] (3) 0/0 - 1/2")

    def test5_raiseError(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test6_raiseError(self):
        self.assertRaises(TypeError, Rectangle)

    def test7_check_id(self):
        r5 = Rectangle(10, 1)
        self.assertEqual(r5.id, 4)

    def test8_check_id(self):
        r6 = Rectangle(6, 9)
        self.assertEqual(r6.id, 5)

    def test9_check_width(self):
        r7 = Rectangle(6, 9)
        self.assertEqual(r7.width, 6)

    def test10_check_width(self):
        self.assertRaises(ValueError, Rectangle, -3, 8, id=10)

    def test11_check_length(self):
        r8 = Rectangle(6, 9, id=11)
        self.assertEqual(r8.height, 9)

    def test12_check_length(self):
        self.assertRaises(ValueError, Rectangle, 3, -6, id=11)
