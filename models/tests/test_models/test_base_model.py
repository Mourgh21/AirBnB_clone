#!/usr/bin/python3
"""Unit test for BaseModel"""

import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys
from unittest.mock import patch

# Redirecting stdout for capturing output
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """Test case for BaseModel class"""

    def setUp(self):
        """Set up the test environment"""
        # Clearing storage and resetting file
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        """Tear down the test environment"""
        # Restoring stdout and capturing output
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        """Test initialization of BaseModel instance"""
        # Create a new BaseModel instance
        new = BaseModel()

        # Check existence of required methods and attributes
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        # Check types of attributes
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)

        # Check if instance is saved in storage
        keyname = "BaseModel." + new.id
        self.assertIn(keyname, models.storage.all())
        self.assertTrue(models.storage.all()[keyname] is new)

        # Test attribute update and save
        new.name = "My First Model"
        new.my_number = 89
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "name"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "my_number"))

        old_time = new.updated_at
        new.save()
        self.assertNotEqual(old_time, new.updated_at)
        self.assertGreater(new.updated_at, old_time)

        # Check if save() calls models.storage.save()
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        # Check if instance is saved in JSON file
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname], new.to_dict())

    def test_basemodel_init2(self):
        """Test initialization of BaseModel instance from dictionary"""
        # Create a new BaseModel instance and update its attributes
        new = BaseModel()
        new.name = "John"
        new.my_number = 89

        # Create a new BaseModel instance from dictionary representation
        new2 = BaseModel(**new.to_dict())

        # Check equality of attributes
        self.assertEqual(new.id, new2.id)
        self.assertEqual(new.name, "John")
        self.assertEqual(new.my_number, 89)
        self.assertEqual(new.to_dict(), new2.to_dict())

    def test_basemodel_init3(self):
        """Test initialization of BaseModel instance from dictionary"""
        # Create a new BaseModel instance
        new = BaseModel()
        
        # Create a new BaseModel instance from dictionary representation
        new2 = BaseModel(new.to_dict())

        # Check inequality of instances and non-equality of IDs
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        
        # Check if created_at and updated_at are datetime instances
        self.assertTrue(isinstance(new2.created_at, datetime))
        self.assertTrue(isinstance(new2.updated_at, datetime))

        # Check string representation
        self.assertEqual(str(new),  "[BaseModel] ({}) {}".format(new.id, new.__dict__))

        # Check if updated_at changes after save()
        old_time = new.updated_at
        new.save()
        self.assertGreater(new.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
