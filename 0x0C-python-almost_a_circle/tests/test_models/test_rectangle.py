#!/usr/bin/python3

"""
Unittesting for class Rectangle
"""

import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangleClass(unittest.TestCase):
    """
    Test class for rectangle
    """

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

    def test_check_width_TypeError_02(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'width must be an integer',
                               Rectangle,
                               [6, 4, 9, 9], 2, 0, 0, 12)

    def test_check_width_ValueError(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(ValueError,
                               'width must be > 0',
                               Rectangle,
                               -1, 2, 0, 0, 12)

    def test_check_height_TypeError_01(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'height must be an integer',
                               Rectangle,
                               2, 'string', 0, 0, 12)

    def test_check_height_TypeError_02(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'height must be an integer',
                               Rectangle,
                               3, [1, 2, 3, 4], 0, 0, 12)

    def test_check_height_ValueError(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(ValueError,
                               'height must be > 0',
                               Rectangle,
                               1, -2, 0, 0, 12)

    def test_check_x(self):
        """Test x of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(2, 10, 6)
        self.assertEqual(r2.x, 6)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.x, 3)

        r4 = Rectangle(5, 2, 0, 3, 12)
        self.assertEqual(r4.x, 0)

    def test_check_x_TypeError_01(self):
        """Test TypeError for x in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'x must be an integer',
                               Rectangle,
                               4, 2, 'string''', 0, 12)

    def test_check_x_TypeError_02(self):
        """Test TypeError for x in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'x must be an integer',
                               Rectangle,
                               4, 2, [1, 2, 3, 4], 0, 12)

    def test_check_x_ValueError(self):
        """Test ValueError for x in Rectangle"""
        self.assertRaisesRegex(ValueError,
                               'x must be >= 0',
                               Rectangle,
                               4, 2, -1, 0, 12)

    def test_check_y(self):
        """Test y of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 6, 4)
        self.assertEqual(r2.y, 4)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.y, 9)

        r4 = Rectangle(5, 2, 3, 0, 12)
        self.assertEqual(r4.y, 0)

    def test_check_y_TypeError_01(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'y must be an integer',
                               Rectangle,
                               4, 2, 0, 'string', 12)

    def test_check_y_TypeError_02(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'y must be an integer',
                               Rectangle,
                               4, 2, 0, [1, 2, 3, 4], 12)

    def test_check_y_TypeError_(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(ValueError,
                               'y must be >= 0',
                               Rectangle,
                               4, 2, 0, -6, 12)

    def test_update(self):
        """Test update"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_extra(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6, 7)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_no_param(self):
        """Update with extra parameters"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (20) 10/10 - 10/10")

    def test_kwargs(self):
        """Test kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (16) 1/3 - 4/2")

    def test_kwargs_extra_keys(self):
        """Test kwargs with extra parameters"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, banu=89)
        self.assertEqual(str(r1), "[Rectangle] (17) 1/3 - 4/2")

    def test_inputs50(self):
        """test inputs square class"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r2), "[Rectangle] (11) 3/4 - 1/2")
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(str(r3), "[Rectangle] (12) 3/0 - 1/2")
        r4 = Rectangle(1, 2)
        self.assertEqual(str(r4), "[Rectangle] (13) 0/0 - 1/2")

    def test_inputs51(self):
        """test inputs square class"""
        b1 = Base()
        result = b1.id
        self.assertIs(result, 14)
        b2 = Base()
        result = b2.id
        self.assertIs(result, 15)
        b3 = Base(12)
        result = b3.id
        self.assertIs(result, 12)

if __name__ == '__main__':
    unittest.main()
