#!/usr/bin/python3
"""
Unit tests
"""


import unittest
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    """class"""
    def test_presence_of_module_docstring(self):
        """module docstring"""
        module_doc = base.__doc__
        self.assertTrue(len(module_doc) > 1)

if __name__ == "__main__":
    unittest.main()
