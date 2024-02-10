#!/usr/bin/python3
"""Defining unittest for the file rectangle.py"""
import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)


if __name__ == '__main__':
    unittest.main()