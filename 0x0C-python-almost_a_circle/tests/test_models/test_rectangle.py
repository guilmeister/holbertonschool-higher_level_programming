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
        """Full attributes"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

    def test2_inputs_correct(self):
        """Missing ID"""
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r2), "[Rectangle] (1) 3/4 - 1/2")

    def test3_inputs_correct(self):
        """Missing ID, y"""
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(str(r3), "[Rectangle] (2) 3/0 - 1/2")

    def test4_inputs_correct(self):
        """Missing ID, y, x"""
        r4 = Rectangle(1, 2)
        self.assertEqual(str(r4), "[Rectangle] (3) 0/0 - 1/2")

    def test5_raiseError(self):
        """Raise error on missing height"""
        self.assertRaises(TypeError, Rectangle, 1)

    def test6_raiseError(self):
        """Raise error on missing width"""
        self.assertRaises(TypeError, Rectangle)

    def test7_check_id(self):
        """Check ID count"""
        r5 = Rectangle(10, 1)
        self.assertEqual(r5.id, 4)

    def test8_check_id(self):
        """Check increment ID count"""
        r6 = Rectangle(6, 9)
        self.assertEqual(r6.id, 5)

    def test9_check_width(self):
        """Check valid width"""
        r7 = Rectangle(6, 9)
        self.assertEqual(r7.width, 6)

    def test10_check_width(self):
        """Check invalid width"""
        self.assertRaises(ValueError, Rectangle, -3, 8, id=10)

    def test11_check_width(self):
        """Check invalid width string"""
        self.assertRaises(TypeError, Rectangle, "three", 8, id=69)

    def test12_check_length(self):
        """Check valid height"""
        r8 = Rectangle(6, 9, id=11)
        self.assertEqual(r8.height, 9)

    def test13_check_length(self):
        """Check invalid height"""
        self.assertRaises(ValueError, Rectangle, 3, -6, id=11)

    def test14_check_length(self):
        """Check invalid height string"""
        self.assertRaises(TypeError, Rectangle, 3, "three", id=52)

    def test15_check_width(self):
        """Check invalid width list"""
        self.assertRaises(TypeError, Rectangle, [3, 6], 2, id=25)

    def test16_check_height(self):
        """Check invalid height list"""
        self.assertRaises(TypeError, Rectangle, 2, [3, 6], id=100)
