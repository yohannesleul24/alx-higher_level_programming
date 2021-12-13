#!/usr/bin/python3
"""
Real definition of a rectangle

"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """The __init__ method of the square class
        Args:
            width(int): Private attribute default 0
            height(int): Private attribute default 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Private instance attribute getter method."""
        return self.__width

    @property
    def height(self):
        """Private instance attribute getter method."""
        return self.__height

    @width.setter
    def width(self, value):
        """Private instance attribute property setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Private instance attribute property setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Measure area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Measure perimeter."""
        if not (self.__width == 0 or self.__height == 0):
            return ((self.__width + self.__height) * 2)
        return 0

    def __str__(self):
        """String conversion"""
        if self.width == 0 or self.height == 0:
            return ("")
        re = (((str(self.print_symbol) * self.__width) + '\n') * self.__height)
        re = re[:-1]
        return re

    def __repr__(self):
        """Repr"""
        rectangle = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """Delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area
        Args:
            rect_1 (int): Instance of Rectangle
            rect_2 (int): Instance of Rectangle
        Raise: TypeError
        Return: The biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size
        Args:
            size (int): Square size
        Return: A new Rectangle instance with width == height == size
        """
        return Rectangle(size, size)
