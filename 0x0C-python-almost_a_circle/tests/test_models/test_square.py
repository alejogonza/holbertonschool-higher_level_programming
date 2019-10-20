#!/usr/bin/python3
"""
Test for the Square class
"""

import unittest
import pep8
import inspect
import io
import json
import os
from contextlib import redirect_stdout
from models import square
from models.base import Base
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """
    Tests documentation and style
    """
    @classmethod
    def setUpClass(cls):
        """
        Tests documentation and style
        """
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_review_1(self):
        """
        Tests documentation and style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_2(self):
        """
        Tests documentation and style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_3(self):
        """
        Tests documentation and style
        """
        self.assertTrue(len(square.__doc__) >= 1)

    def test_review_4(self):
        """
        Tests documentation and style
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_review_5(self):
        """
        Tests documentation and style
        """
        for func in self.sq_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    """
    Tests documentation and style
    """
    @classmethod
    def setUpClass(cls):
        """
        Tests documentation and style
        """
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_review_6(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

    def test_review_7(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_review_8(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 4)
        self.assertEqual(self.s4.width, 7)

    def test_review_9(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_review_10(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_review_11(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_review_12(self):
        """
        Tests documentation and style
        """
        with self.assertRaises(TypeError):
            s = Square()

    def test_review_13(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("people")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_review_14(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "people")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_review_15(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "people")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, True)

    def test_review_16(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_review_17(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_review_18(self):
        """
        Tests documentation and style
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_review_19(self):
        """
        Tests documentation and style
        """
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 49)

    def test_review_20(self):
        """
        Tests documentation and style
        """
        with self.assertRaises(TypeError):
            a = self.s1.area(1)

    def test_review_21(self):
        """
        Tests documentation and style
        """
        s = Square(3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s1.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_review_22(self):
        """
        Tests documentation and style
        """
        with self.assertRaises(TypeError):
            self.s1.display(1)

    def test_review_23(self):
        """
        Tests documentation and style
        """
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (3) 5/6 - 4")
        self.assertEqual(str(self.s4), "[Square] (10) 8/9 - 7")

    def test_review_24(self):
        """
        Tests documentation and style
        """
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 3 + "#" * 2 + "\n") * 2)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.s3.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 6 +
                             (" " * 5 + "#" * 4 + "\n") * 4)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.s4.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 9 +
                             (" " * 8 + "#" * 7 + "\n") * 7)

    def test_review_25(self):
        """
        Tests documentation and style
        """
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/0 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_review_26(self):
        """
        Tests documentation and style
        """
        s = Square(1, 0, 0, 1)
        with self.assertRaises(TypeError):
            s.update(1, "people")
        with self.assertRaises(TypeError):
            s.update(1, 1, "people")
        with self.assertRaises(TypeError):
            s.update(1, 1, 1, "people")
        with self.assertRaises(ValueError):
            s.update(1, 0)
        with self.assertRaises(ValueError):
            s.update(1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, 1, -1)

    def test_review_27(self):
        """
        Tests documentation and style
        """
        s = Square(1, 0, 0, 1)
        s.update(1, 1, 1, 1, 2)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")

    def test_review_28(self):
        """
        Tests documentation and style
        """
        s = Square(1, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_review_29(self):
        """
        Tests documentation and style
        """
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=10)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        s.update(size=11, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 11")
        s.update(y=5, size=7, x=5, id=89)
        self.assertEqual(str(s), "[Square] (9) 5/5 - 7")

    def test_review_30(self):
        """
        Tests documentation and style
        """
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.update(size="people")
        with self.assertRaises(TypeError):
            s.update(x="people")
        with self.assertRaises(TypeError):
            s.update(y="people")
        with self.assertRaises(ValueError):
            s.update(size=-1)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-1)
        with self.assertRaises(ValueError):
            s.update(y=-1)

    def test_review_31(self):
        """
        Tests documentation and style
        """
        s = Square(1, 0, 0, 1)
        s.update(2, 2, 2, 2, size=3, x=3, y=3, id=3)
        self.assertEqual(str(s), "[Square] (3) 3/3 - 3")

    def test_review_32(self):
        """
        Tests documentation and style
        """
        s = Square(1, 1, 1, 1)
        s.update(people=2)
        self.assertEqual(str(s), "[Square] (1) 1/1 - 1")

    def test_review_33(self):
        """
        Tests documentation and style
        """
        d1 = self.s1.to_dictionary()
        self.assertEqual({"id": 2, "size": 1, "x": 0, "y": 0}, d1)
        d2 = self.s2.to_dictionary()
        self.assertEqual({"id": 5, "size": 2, "x": 2, "y": 2}, d2)
        d3 = self.s3.to_dictionary()
        self.assertEqual({"id": 8, "size": 1, "x": 1, "y": 1}, d3)
        d4 = self.s4.to_dictionary()
        self.assertEqual({"id": 9, "size": 9, "x": 9, "y": 9}, d4)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)
        self.assertTrue(type(d3) is dict)
        self.assertTrue(type(d4) is dict)
        s = Square(1, 1, 1, 1)
        s.update(**d4)
        self.assertEqual(str(s), str(self.s4))
        self.assertNotEqual(s, self.s4)

    def test_review_34(self):
        """
        Tests documentation and style
        """
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        l = [s1, s2]
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            ls = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_review_35(self):
        """
        Tests documentation and style
        """
        l = []
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_review_36(self):
        """
        Tests documentation and style
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_review_37(self):
        """
        Tests documentation and style
        """
        s1 = {"id": 8, "size": 1, "x": 1, "y": 1}
        s2 = {"id": 9, "size": 9, "x": 9, "y": 9}
        s1c = Square.create(**s1)
        s2c = Square.create(**s2)
        self.assertEqual("[Square] (8) 1/1 - 1", str(s1c))
        self.assertEqual("[Square] (9) 9/9 - 9", str(s2c))
        self.assertIsNot(s1, s1c)
        self.assertIsNot(s2, s2c)
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)

    def test_review_38(self):
        """
        Tests documentation and style
        """
        try:
            os.remove("Square.json")
        except:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_review_39(self):
        """Tests documentation and style"""
        try:
            os.remove("Square.json")
        except:
            pass
        open("Square.json", 'a').close()
        self.assertEqual(Square.load_from_file(), [])

    def test_review_40(self):
        """
        Tests documentation and style
        """
        s1 = Square(8, 1, 1, 1)
        s2 = Square(9, 9, 9, 9)
        lif = [s1, s2]
        Square.save_to_file(lif)
        lof = Square.load_from_file()
        self.assertTrue(type(lof) is list)
        self.assertEqual(len(lof), 2)
        s1c = lof[0]
        s2c = lof[1]
        self.assertTrue(type(s1c) is Square)
        self.assertTrue(type(s2c) is Square)
        self.assertEqual(str(s1), str(s1c))
        self.assertEqual(str(s2), str(s2c))
        self.assertIsNot(s1, s1c)
        self.assertIsNot(s2, s2c)
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)
