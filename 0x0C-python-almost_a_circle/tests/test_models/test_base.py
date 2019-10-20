#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import inspect
import pep8
import json
from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """\nTests documentation and style\n"""
    @classmethod
    def setUpClass(cls):
        """
        Tests documentation and style
        """
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_review_1(self):
        """
        Tests documentation and style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_2(self):
        """
        Tests documentation and style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_3(self):
        """
        Tests documentation and style
        """
        self.assertTrue(len(base.__doc__) >= 1)

    def test_review_4(self):
        """
        Tests documentation and style
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_review_5(self):
        """
        Tests documentation and style
        """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """
    Tests documentation and style
    """
    def test_review_6(self):
        """
        Tests documentation and style
        """
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_review_7(self):
        """
        Tests documentation and style
        """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_review_8(self):
        """
        Tests documentation and style
        """
        b16 = Base(16)
        self.assertEqual(b16.id, 16)

    def test_review_9(self):
        """
        Tests documentation and style
        """
        b8 = Base()
        self.assertEqual(b8.id, 8)

    def test_review_10(self):
        """
        Tests documentation and style
        """
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_review_11(self):
        """
        Tests documentation and style
        """
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 9, "height": 9, "x": 9, "y": 9}
        d2 = {"id": 8, "width": 1, "height": 1, "x": 2, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_review_12(self):
        """
        Tests documentation and style
        """
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_review_13(self):
        """
        Tests documentation and style
        """
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_review_14(self):
        """
        Tests documentation and style
        """
        json_str = '[{"id": 9, "width": 9, "height": 9, "x": 9, "y": 9}, \
{"id": 8, "width": 1, "height": 1, "x": 2, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 9, "height": 9, "x": 9, "y": 9})
        self.assertEqual(json_l[1],
                         {"id": 8, "width": 1, "height": 1, "x": 2, "y": 0})

    def test_review_15(self):
        """
        Tests documentation and style
        """
        self.assertEqual([], Base.from_json_string(""))

    def test_review_16(self):
        """
        Tests documentation and style
        """
        self.assertEqual([], Base.from_json_string(None))
