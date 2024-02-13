#!/usr/bin/python3
"""Defining unittest for the file rectangle.py"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unittest for the rectangle func."""
    def test_2_args(self):
        My_rect = Rectangle(77, 99)
        self.assertEqual(My_rect.width, 77)
        self.assertEqual(My_rect.height, 99)
        self.assertEqual(My_rect.x, 0)
        self.assertEqual(My_rect.y, 0)
    
    def test_4_args(self):
        My_rect = Rectangle(77, 99, 8, 1)
        self.assertEqual(My_rect.width, 77)
        self.assertEqual(My_rect.height, 99)
        self.assertEqual(My_rect.x, 8)
        self.assertEqual(My_rect.y, 1)



if __name__ == '__main__':
    unittest.main()
