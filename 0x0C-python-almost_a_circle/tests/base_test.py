#!/usr/bin/python3
"""
Tests for class base, the base class of all other classes
"""


import unittest
base_test = __import__('base').base_test


class TestBase(unittest.TestCase):
    """tests for base class"""
    def test_id_incremented_correctly(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)
