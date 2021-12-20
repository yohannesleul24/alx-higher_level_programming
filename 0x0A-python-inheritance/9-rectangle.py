#!/usr/bin/python3
"""
Rectangle module

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass Rectangle from class BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation, constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area method"""
        return (self.__width * self.__height)

    def __str__(self):
        """Print"""
        return ('[Rectangle] {}/{}'.format(str(self.__width),
                                           str(self.__height)))
