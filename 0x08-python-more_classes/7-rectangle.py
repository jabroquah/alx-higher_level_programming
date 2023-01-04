#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """A rectangle template"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (2 * self.__height))

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")

        final = ['#' * self.__width for line in range(self.__height)]
        return '\n'.join(final)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
