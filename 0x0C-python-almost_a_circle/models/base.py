#!/usr/bin/python3
"""
Class Base
"""

import json
import turtle
import csv


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        A representation of a rectangle
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dicc):
        """
        returns the JSON string
        """
        if list_dicc is None:
            list_dicc = []
        return json.dumps(list_dicc)

    @staticmethod
    def from_json_string(json_s):
        """
        returns the list of the JSON string
        """
        if json_s is None or len(json_s) == 0:
            return []
        return json.loads(json_s)

    @classmethod
    def save_to_file(classes, list_ob):
        """
        writes the JSON string
        """
        filename = classes.__name__ + ".json"
        lo = []
        if list_ob is not None:
            for i in list_ob:
                lo.append(classes.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(classes.to_json_string(lo))

    @classmethod
    def create(cls, **dictionary):
        """ instance """
        if cls.__name__ == "Rectangle":
            newc = cls(10, 10)
        else:
            newc = cls(10)
        newc.update(**dictionary)
        return newc

    @classmethod
    def load_from_file(cls):
        """ open and create instance """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(classes, list_ob):
        """
        serializes a list of Rectangles/Squares in csv
        """
        filename = classes.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if classes.__name__ is "Rectangle":
                for obj in list_ob:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif classes.__name__ is "Square":
                for obj in list_ob:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(classes):
        """
        deserializes a list Class in csv
        """
        filename = classes.__name__ + ".csv"
        l2 = []
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for args in csv_reader:
                if classes.__name__ is "Rectangle":
                    dictionary = {
                                    "id": int(args[0]),
                                    "width": int(args[1]),
                                    "height": int(args[2]),
                                    "x": int(args[3]),
                                    "y": int(args[4])}
                elif classes.__name__ is "Square":
                    dictionary = {
                                    "id": int(args[0]),
                                    "size": int(args[1]),
                                    "x": int(args[2]),
                                    "y": int(args[3])}
                obj = classes.create(**dictionary)
                l2.append(obj)
        return l2
