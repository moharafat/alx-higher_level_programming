#!/usr/bin/python3
"""Defining unittest for the file rectangle.py"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    @classmethod
    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(r.width, 10)

if __name__ == '__main__':
    unittest.main()
