#!/usr/bin/python3
"""Unit test for State"""

import unittest
from models.state import State
from datetime import datetime


class StateTestCase(unittest.TestCase):
    """Test case for State class"""

    def test_state(self):
        """Test State instance attributes"""
        # Create a new State instance
        new = State()

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
