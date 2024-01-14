#!/usr/bin/python3
"""test cases for class rectangle"""


import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle_width(unittest.TestCase):
    """unittests for testing the width attribute"""
    def test_none_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.2, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(3), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(6), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 3, "b": 6}, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)


class TestRectangle_height(unittest.TestCase):
    """unittests for testing the height attribute"""

    def test_none_width(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "height")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 2.2)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [1, 2, 3])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 2, 3})

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(3))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(6))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 3, "b": 6})

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)


class TestRectangle_x(unittest.TestCase):
    """unittests for testing the x attribute"""

    def test_none_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None, 2)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "width", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 2.2, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(3), 2)

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(6), 2)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 3, "b": 6}, 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3, 2)


class TestRectangle_y(unittest.TestCase):
    """unittests for testing the width attribute"""

    def test_none_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, "width")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, 2.2)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {1, 2, 3})

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(3))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(6))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 4, {"a": 3, "b": 6})

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 4, -3)


class TestRectangle_area(unittest.TestCase):
    """class to test the area of the rectangle"""

    def test_small_area(self):
        r = Rectangle(6, 8, 3, 4)
        self.assertEqual(48, r.area())

    def test_large_area(self):
        r = Rectangle(999999, 999999, 3, 4)
        self.assertEqual(999998000001, r.area())

    def test_area_args_changed(self):
        r = Rectangle(3, 4, 3, 9)
        r.width = 7
        r.height = 3
        self.assertEqual(21, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 3)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """
    unittest for testing display of rectngle display using '#' character
    """

    def setUp(self):
        self.capture = sys.stdout

    def tearDown(self):
        sys.stdout = self.capture

    def test_display_width_height(self):
        r = Rectangle(3, 2)
        capture = StringIO()
        sys.stdout = capture
        r.display()
        sys.stdout = sys.__stdout__
        output = capture.getvalue()
        self.assertEqual("###\n###\n", output)

    def test_display_width_height_reversed(self):
        r = Rectangle(2, 3)
        capture = StringIO()
        sys.stdout = capture
        r.display()
        sys.stdout = sys.__stdout__
        output = capture.getvalue()
        self.assertEqual("##\n##\n##\n", output)

    def test_str_method_width_height(self):
        r = Rectangle(2, 3)
        captured = StringIO()
        sys.stdout = captured
        print(r)
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        correct = "[Rectangle] ({}) 0/0 - 2/3\n".format(r.id)
        self.assertEqual(correct, output)

    def test_str_method_width_height_x(self):
        r = Rectangle(2, 3, 4)
        captured = StringIO()
        sys.stdout = captured
        print(r)
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        correct = "[Rectangle] ({}) 4/0 - 2/3\n".format(r.id)
        self.assertEqual(correct, output)

    def test_str_method_width_height_x_y(self):
        r = Rectangle(2, 3, 4, 5)
        captured = StringIO()
        sys.stdout = captured
        print(r)
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        correct = "[Rectangle] ({}) 4/5 - 2/3\n".format(r.id)
        self.assertEqual(correct, output)

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(2, 3, 4, 5, 7)
        captured = StringIO()
        sys.stdout = captured
        print(r)
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        correct = "[Rectangle] (7) 4/5 - 2/3\n"
        self.assertEqual(correct, output)

    def test_str_method_width_height_x_y(self):
        r = Rectangle(2, 3, 4, 5, 8)
        r.width = 10
        r.height = 11
        r.x = 12
        r.y = 13
        self.assertEqual("[Rectangle] (8) 12/13 - 10/11", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)
