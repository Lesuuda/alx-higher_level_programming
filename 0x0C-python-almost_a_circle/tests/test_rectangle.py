#!/usr/bin/python3
"""tests for class rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests for class rectangle"""
    def test_width_getter_setter(self):
        """tests for the effectiveness of width getter and setter"""
        r1 = Rectangle(width=5, height=10)
        r1.width = 15
        self.assertEqual(r1.width, 15)

    def test_height_getter_setter(self):
        """tests for the effectiveness of height getter and setter"""
        r1 = Rectangle(width=5, height=10)
        r1.height = 15
        self.assertEqual(r1.height, 15)

    def test_x_getter_setter(self):
        """tests for the effectiveness of x getter and setter"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r1.x = 15
        self.assertEqual(r1.x, 15)

    def test_y_getter_setter(self):
        """tests for the effectiveness of y getter and setter"""
        r1 = Rectangle(10, 2, 3, 4, 12)
        r1.y = 15
        self.assertEqual(r1.y, 15)

    def test_id_setter(self):
        """tests for effectiveness of id setter"""
        r1 = Rectangle(10, 2, 3, 4, 12)
        r1.id = 100
        self.assertEqual(r1.id, 100)

    def test_width_negative_value(self):
        """tets for width negative value"""
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(width=-5, height=10, x=3, y=4, id=12)
        self.assertIn("width must be > 0", str(context.exception))

    def test_height_nagative_value(self):
        """tets for height negative value"""
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(5, -10, 3, 4, 12)
        self.assertIn("height must be > 0", str(context.exception))

    def test_x_nagative_value(self):
        """tets for x negative value"""
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(5, 10, -3, 4, 12)
        self.assertIn("x must be >= 0", str(context.exception))

    def test_y_nagative_value(self):
        """tets for y negative value"""
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(5, 10, 3, -4, 12)
        self.assertIn("y must be >= 0", str(context.exception))

    def test_width_zero_value(self):
        """tets for width zero  value"""
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(0, 10, 3, 4, 12)
        self.assertIn("width must be > 0", str(context.exception))

    def test_height_zero_value(self):
        """tets for height negative value"""
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(5, 0, 3, 4, 12)
        self.assertIn("height must be > 0", str(context.exception))
