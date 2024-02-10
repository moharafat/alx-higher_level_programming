#!/usr/bin/python3
"""Defining unittest for the file rectangle.py"""
import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    def test_width_getter(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(1, r1.id)


if __name__ == '__main__':
    unittest.main()