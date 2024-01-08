#!/usr/bin/python3
"""
unittest for function that checks for the largest integer in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TetstMaxInteger(unittest.TestCase):
    """tests for the max integer in a list"""

    def test_is_empty(self):
        """tests for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """tests for the max number in a single element list"""
        self.assertEqual(max_integer([4]), 4)

    def test_positive_numbers(self):
        """tests for the max int in a list of lositive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_negative_numbers(self):
        """tests for the max int in a list of negative numbers"""
        self.assertEqual(max_integer([-2, -1, -5]), -1)

    def test_both_postive_and_negative(self):
        """"tests for the max int in a list of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 2, -6]), 2)

    def test_duplicate_numbers(self):
        """tests for the max int in a list of duplicate numbers"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_float(self):
        """tests for the max float in a list of ibtegers"""
        self.assertEqual(max_integer([2.2, 2.4, 2.9]), 2.9)
