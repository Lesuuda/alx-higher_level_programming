#!/usr/bin/python3
"""
Tests for class base, the base class of all other classes
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests for base class"""
    def test_id_incremented_correctly(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_provided(self):
        """test case when the id is provided"""
        custom_id = 24
        b1 = Base(id=custom_id)
        self.assertEqual(b1.id, custom_id)

    def test_id_not_provided(self):
        """test case when id is not provided"""
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)
