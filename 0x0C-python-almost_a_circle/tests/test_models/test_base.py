#!/usr/bin/python3
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_inputs(self):
        b1 = Base()
        result = b1.id
        self.assertIs(result, 1)
        b2 = Base()
        result = b2.id
        self.assertIs(result, 2)
        b3 = Base(12)
        result = b3.id
        self.assertIs(result, 12)
