#!/usr/bin/python3
"""Unit test for City"""

import unittest
from models.city import City
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """Test case for City class"""

    def test_city(self):
        """Test City instance attributes"""
        # Create a new City instance
        new = City()

        # Check existence of required attributes
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "state_id"))
        self.assertTrue(hasattr(new, "name"))

        # Check types of attributes
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.state_id, str)
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
