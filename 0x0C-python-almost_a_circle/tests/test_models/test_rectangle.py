#!/usr/bin/python3
"""Defining unittest for the file rectangle.py"""
import unittest
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout



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

    def test_width_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(-6, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 33)
        with self.assertRaises(TypeError):
            Rectangle("Hello", 5)
            

    def test_height_validation(self):
        # Test height validation
        with self.assertRaises(TypeError):
            Rectangle(4, "aeeq")
        with self.assertRaises(ValueError):
            Rectangle(3, 0)
        with self.assertRaises(ValueError):
            Rectangle(6, -5)


    def test_x_validation(self):
        # Test x validation
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid")
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1)

    def test_y_validation(self):
        # Test y validation
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 6,"invalid")
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 8,-1)

    def test_area(self):
        My_rect = Rectangle(3, 2)
        self.assertEqual(My_rect.area(), 6)
        
    def test_display_no_x_and_y(self):
        Myrec = Rectangle(4, 2)
        The_expected = "####\n####\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            Myrec.display()
            The_Output =  buf.getvalue()
            self.assertEqual(The_Output, The_expected)

    def test_display_no_y(self):
        Myrec = Rectangle(4, 2, 1)
        The_expected = " ####\n ####\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            Myrec.display()
            The_Output =  buf.getvalue()
            self.assertEqual(The_Output, The_expected)

    def test_display_Full(self):
        Myrec = Rectangle(4, 2, 1, 2)
        The_expected = "\n\n ####\n ####\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            Myrec.display()
            The_Output =  buf.getvalue()
            self.assertEqual(The_Output, The_expected)
if __name__ == '__main__':
    unittest.main()
