#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Def.Unittest for max_integer([..]"""

    def test_ordered(self):
        """list made out of int [orderd]"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)
    
    def test_max_begining(self):
        max_at_begining = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begining), 4)

    def test_unordered(self):
        """LIST MADE OUT OF INT BUT [UNORDERED]"""
        unordered = [2,4,3,1]
        self.assertEqual(max_integer(unordered), 4)

    def test_only_1_elment(self):
        only_1 = [9]
        self.assertEqual(max_integer(only_1), 9)

    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_float_list(self):
        floaty = [33.4, 55.2, 44.9, 11.7]
        self.assertEqual(max_integer(floaty), 55.2)
    
    def test_floats_and_integers(self):
        floaty_and_inty = [3, 77.3, 11.3, 99]
        self.assertEqual(max_integer(floaty_and_inty), 99)
 
    def test_strings(self):
        strin = ["Gamed"]
        self.assertEqual(max_integer(strin), "Gamed")

    def test_list_of_strings(self):
        strings = ["7mao", "Hello", "123456789", "Ahmed"]
        self.assertEqual(max_integer(strings), "Ahmed")
    
    def test_no_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()