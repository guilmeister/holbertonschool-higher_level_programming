#!/usr/bin/python3

"""
Unittesting for class square
"""

import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    class testing for valid/invalid outputs
    """
    def test1_inputs(self):
        """square valid input"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test2_inputs(self):
        """square negative input"""
        self.assertRaises(ValueError, Square, -5)

    def test3_inputs(self):
        """square string input"""
        self.assertRaises(TypeError, Square, "five")

    def test4_inputs(self):
        """square list input"""
        self.assertRaises(TypeError, Square, [69, 619])

    def test5_inputs(self):
        """check string output"""
        s2 = Square(6)
        self.assertEqual(str(s2), "[Square] (3) 0/0 - 6")

    def test6_updates(self):
        """check if updates args"""
        s3 = Square(3)
        s3.update(69)
        self.assertEqual(s3.id, 69)

    def test7_updates(self):
        """check if updates kwargs"""
        s4 = Square(size=5)
        s4.update(size=551)
        self.assertEqual(s4.size, 551)

    def test8_updates(self):
        """check multiple args"""
        s5 = Square(1, 2, 3, 4)
        s5.update(5, 6, 7, 8)
        self.assertEqual(str(s5), "[Square] (5) 7/8 - 6")

    def test9_updates(self):
        """check multiple kwargs"""
        s6 = Square(2)
        s6.update(id=5, size=2, x=4, y=6)
        self.assertEqual(str(s6), "[Square] (5) 4/6 - 2")

    def test10_updates(self):
        """check 2 kwargs update"""
        s7 = Square(3)
        s7.update(size=69, id=4)
        self.assertEqual(str(s7), "[Square] (4) 0/0 - 69")
