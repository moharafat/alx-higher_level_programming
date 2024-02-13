#!/usr/bin/python3
"""Defining unittest for the file rectangle.py"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unittest for the rectangle func."""
    def test_2_args(self):
        My_rect = Rectangle(88, 77)
        self.assertEqual(My_rect.width, 88)
        self.assertEqual(My_rect.height, 77)

    
    def test_4_args(self):
        My_rect = Rectangle(88, 77, 8)
        self.assertEqual(My_rect.width, 88)
        self.assertEqual(My_rect.height, 77)
        self.assertEqual(My_rect.x, 8)
        self.assertEqual(My_rect.y, 0)

    def test_4_args(self):
        My_rect = Rectangle(88, 77, 8, 1)
        self.assertEqual(My_rect.width, 88)
        self.assertEqual(My_rect.height, 77)
        self.assertEqual(My_rect.x, 8)
        self.assertEqual(My_rect.y, 1)

    def test_5_args(self):
        My_rect = Rectangle(99, 88, 77, 55, 1)
        self.assertEqual(My_rect.width, 99)
        self.assertEqual(My_rect.height, 88)
        self.assertEqual(My_rect.x, 77)
        self.assertEqual(My_rect.y, 55)
        self.assertEqual(My_rect.id, 1)
    
    def test_3_args_str(self):
        with self.assertRaises(TypeError):
            My_rect = Rectangle(99, 88, "Hello")

    def test_height_validation(self):
        # Test height validation
        with self.assertRaises(TypeError):
            Rectangle(5, "alx")

if __name__ == '__main__':
    unittest.main()
