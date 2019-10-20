#!/usr/bin/python3
"""
Test for the Rectangle class
"""

import unittest
import pep8
import inspect
import io
import json
import os
from contextlib import redirect_stdout
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """
    Tests documentation and style
    """
    @classmethod
    def setUpClass(cls):
        """
        Tests documentation and style
        """
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_review_1(self):
        """
        Tests documentation and style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_2(self):
        """
        Tests documentation and style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_3(self):
        """
        Tests documentation and style
        """
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_review_4(self):
        """
        Tests documentation and style
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_review_5(self):
        """
        Tests documentation and style
        """
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """
    Tests documentation and style
    """
    @classmethod
    def setUpClass(cls):
        """"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_review_6(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 9)
        self.assertEqual(self.r4.id, 3)

    def test_review_7(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r4.width, 2)

    def test_review_8(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r3.height, 8)
        self.assertEqual(self.r4.height, 7)

    def test_review_9(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 13)

    def test_review_10(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 14)

    def test_review_11(self):
        """
        Tests documentation and style
        """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_review_12(self):
        """
        Tests documentation and style
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_review_13(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("people", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)

    def test_review_14(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "people")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)

    def test_review_15(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "people")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, True)

    def test_review_16(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "people")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, True)

    def test_review_17(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_review_18(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_review_19(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_review_20(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_review_21(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.r1.area(), 25)
        self.assertEqual(self.r2.area(), 9)
        self.assertEqual(self.r3.area(), 56)
        self.assertEqual(self.r4.area(), 14)

    def test_review_22(self):
        """
        Tests documentation and style
        """
        with self.assertRaises(TypeError):
            r = self.r1.area(1)

    def test_review_23(self):
        """
        Tests documentation and style
        """
        r = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 10 + "\n") * 10)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_review_24(self):
        """
        Tests documentation and style
        """
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_review_25(self):
        """
        Tests documentation and style
        """
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 5/5")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 3/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/8")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 2/7")

    def test_review_26(self):
        """
        Tests documentation and style
        """
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 4 + "#" * 2 + "\n") * 3)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r3.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 8 +
                             (" " * 7 + "#" * 5 + "\n") * 6)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r4.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 14 +
                             (" " * 13 + "#" * 11 + "\n") * 12)

    def test_review_27(self):
        """
        Tests documentation and style
        """
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(101)
        self.assertEqual(str(r), "[Rectangle] (101) 0/0 - 1/1")
        r.update(101, 2)
        self.assertEqual(str(r), "[Rectangle] (101) 0/0 - 2/1")
        r.update(101, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (101) 0/0 - 2/3")
        r.update(101, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (101) 4/0 - 2/3")
        r.update(101, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (101) 4/5 - 2/3")

    def test_review_28(self):
        """
        Tests documentation and style
        """
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "people")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "people")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "people")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "people")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_review_29(self):
        """
        Tests documentation and style
        """
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_review_30(self):
        """
        Tests documentation and style
        """
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_review_31(self):
        """
        Tests documentation and style
        """
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        r.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        r.update(y=3, width=4, x=5, id=101)
        self.assertEqual(str(r), "[Rectangle] (101) 5/3 - 4/10")
        r.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(r), "[Rectangle] (101) 6/8 - 9/7")

    def test_review_32(self):
        """
        Tests documentation and style
        """
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.update(width="people")
        with self.assertRaises(TypeError):
            r.update(height="people")
        with self.assertRaises(TypeError):
            r.update(x="people")
        with self.assertRaises(TypeError):
            r.update(y="people")
        with self.assertRaises(ValueError):
            r.update(width=-1)
        with self.assertRaises(ValueError):
            r.update(width=0)
        with self.assertRaises(ValueError):
            r.update(height=-1)
        with self.assertRaises(ValueError):
            r.update(height=0)
        with self.assertRaises(ValueError):
            r.update(x=-1)
        with self.assertRaises(ValueError):
            r.update(y=-1)

    def test_review_33(self):
        """
        Tests documentation and style
        """
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_review_34(self):
        """
        Tests documentation and style
        """
        r = Rectangle(1, 0, 0, 1, 1)
        r.update(people=4)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_review_35(self):
        """
        Tests documentation and style
        """
        dic1 = self.r1.to_dictionary()
        self.assertEqual({"id": 8, "width": 1, "height": 1, "x": 1, "y": 0},
                         dic1)
        dic2 = self.r2.to_dictionary()
        self.assertEqual({"id": 2, "width": 2, "height": 2, "x": 2, "y": 2},
                         dic2)
        dic3 = self.r3.to_dictionary()
        self.assertEqual({"id": 9, "width": 9, "height": 9, "x": 9, "y": 9},
                         dic3)
        dic4 = self.r4.to_dictionary()
        self.assertEqual({"id": 4, "width": 4, "height": 4, "x": 4,
                          "y": 4}, dic4)
        self.assertTrue(type(dic1) is dict)
        self.assertTrue(type(dic2) is dict)
        self.assertTrue(type(dic3) is dict)
        self.assertTrue(type(dic4) is dict)
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(**d4)
        self.assertEqual(str(r), str(self.r4))
        self.assertNotEqual(r, self.r4)

    def test_review_36(self):
        """
        Tests documentation and style
        """
        r1 = Rectangle(8, 1, 1, 1, 0)
        r2 = Rectangle(9, 9, 9, 9, 9)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_review_37(self):
        """
        Tests documentation and style
        """
        l = []
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_review_38(self):
        """
        Tests documentation and style
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_review_39(self):
        """
        Tests documentation and style
        """
        r1 = {"id": 8, "width": 1, "height": 1, "x": 2, "y": 0}
        r2 = {"id": 9, "width": 9, "height": 9, "x": 9, "y": 9}
        r1c = Rectangle.create(**r1)
        r2c = Rectangle.create(**r2)
        self.assertEqual("[Rectangle] (2) 4/0 - 2/3", str(r1c))
        self.assertEqual("[Rectangle] (9) 7/8 - 5/6", str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)

    def test_review_40(self):
        """
        Tests documentation and style
        """
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_review_41(self):
        """
        Tests documentation and style
        """
        try:
            os.remove("Rectangle.json")
        except:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_review_42(self):
        """
        Tests documentation and style
        """
        r1 = Rectangle(8, 1, 1, 2, 0)
        r2 = Rectangle(9, 9, 9, 9, 9)
        li = [r1, r2]
        Rectangle.save_to_file(li)
        lo = Rectangle.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        r1c = lo[0]
        r2c = lo[1]
        self.assertTrue(type(r1c) is Rectangle)
        self.assertTrue(type(r2c) is Rectangle)
        self.assertEqual(str(r1), str(r1c))
        self.assertEqual(str(r2), str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)
