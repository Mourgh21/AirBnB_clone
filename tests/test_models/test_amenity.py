#!/usr/bin/python3
"""Unit test for Amenity"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class AmenityTestCase(unittest.TestCase):
    """Test case for Amenity class"""

    def test_amenity(self):
        """Test Amenity instance attributes"""
        # Create a new Amenity instance
        new = Amenity()

        # Check existence of required attributes
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

        # Check types of attributes
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
