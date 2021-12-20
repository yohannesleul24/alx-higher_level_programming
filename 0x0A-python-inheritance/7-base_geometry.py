#!/usr/bin/python3
"""
Geometry module

"""


class BaseGeometry():
    """class BaseGeometry"""

    def area(self):
        """Public instance method Raise Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method validates value"""
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
