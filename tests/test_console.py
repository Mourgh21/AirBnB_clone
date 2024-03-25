import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommandPrompt(unittest.TestCase):
    """Testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandHelp(unittest.TestCase):
    """Testing help messages of the HBNB command interpreter."""

    def test_help(self):
        expected = (
            "Documented commands (type help <topic>):\n"
            "========================================\n"
            "EOF  all  clear  create  destroy  help  quit  show  update"
        )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_help_quit(self):
        expected = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_help_EOF(self):
        expected = "Ctrl-D to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_help_create(self):
        expected = (
            "Creates a new instance :\n"
            "Usage: create <class name>"
        )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(expected, output.getvalue().strip())

    # Add other help test cases


class ConsoleTestCase(unittest.TestCase):
    """Testing errors"""

    def check_json(self, classname, id):
        keyname = f"{classname}.{id}"
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname]["id"], id)
        self.assertEqual(saved_data[keyname]["__class__"], classname)

    def test_error(self):
        """Testing errors"""
        cmd_classname = ["create", "update", "show", "destroy"]
        cmd_id = ["update", "show", "destroy"]
        cmd_attr = ["update"]
        
        # Add your error test cases

    def test_create_object(self):
        """Testing for create"""
        # Add your create object test cases


if __name__ == '__main__':
    unittest.main()
