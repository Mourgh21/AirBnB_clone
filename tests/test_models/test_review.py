#!/usr/bin/python3
"""Unit test for Review"""

import unittest
from models.review import Review
from datetime import datetime


class ReviewTestCase(unittest.TestCase):
    """Test case for Review class"""

    def test_review(self):
        """Test Review instance attributes"""
        # Create a new Review instance
        new = Review()

        # Check existence of required attributes
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "place_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "text"))

        # Check types of attributes
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.place_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.text, str)


if __name__ == '__main__':
    unittest.main()
