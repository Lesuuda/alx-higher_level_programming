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

    def test_display_width_height_x_y(self):
        r = Rectangle(3, 2, 4, 5)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        correct = "\n\n\n\n\n    ###\n    ###\n"
        self.assertEqual(output, correct)

    def test_display_width_height_x_y_reversed(self):
        r = Rectangle(2, 3, 5, 4)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        correct = "\n\n\n\n     ##\n     ##\n     ##\n"
        self.assertEqual(output, correct)

    def test_display_width_height_x_y_is_0(self):
        r = Rectangle(3, 2, 4)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        correct = "    ###\n    ###\n"
        self.assertEqual(output, correct)

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

    def test_update_no_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update()
        self.assertEqual("[Rectangle] (2) 2/2 - 2/2", str(r))

    def test_update_one_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(16)
        self.assertEqual("[Rectangle] (16) 2/2 - 2/2", str(r))

    def test_update_two_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(16, 19)
        self.assertEqual("[Rectangle] (16) 2/2 - 19/2", str(r))

    def test_update_three_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(16, 19, 20)
        self.assertEqual("[Rectangle] (16) 2/2 - 19/20", str(r))

    def test_update_four_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(16, 19, 20, 21)
        self.assertEqual("[Rectangle] (16) 21/2 - 19/20", str(r))

    def test_update_five_args(self):
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(16, 19, 20, 21, 22)
        self.assertEqual("[Rectangle] (16) 21/22 - 19/20", str(r))

class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


