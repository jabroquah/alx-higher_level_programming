#!/usr/bin/python3
"""Defines a rectangle class."""
from base import Base


class Rectangle(Base):
    """
        A rectangle class
        ...

        Methods
        -------
        set_width(width) : None
            sets width of rectangle
        get_width(): int
            returns the width of the rectangle
        set_height(height): None
            sets height of rectangle
        get_height(): int
            returns the height of the rectangle
        set_x(x): None
            sets the x-position of the rectangle
        get_x(): int
            returns the x-position of the rectangle
        set_y(y): None
            sets the y-position of the rectangle
        get_y(): int
            returns the y-position of the rectangle
        area: int
            returns the area of the rectangle
        display: None
            prints the rectangle size using character #
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Parameters
        ----------
        width: int
            width of the rectangle
        height: int
            height of the rectangle
        x: int, optional
            x-position of the rectangle (default = 0)
        y: int, optional
            y-position of the rectangle (default = 0)
        id: int, optional
            id of the rectangle (default = None)

        Raises
        ------
        ValueError: if x or y is < 0, or width or height <= 0
        TypeError: if input is not an integer
        """
        super().__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def set_width(self, width):
        """
            Sets the width of rectangle object

            Parameters
            ----------
            width: int
                width of the rectangle
        """
        if width <= 0:
            raise ValueError(width,'must be > 0')
        elif type(width) is not int:
            raise TypeError(width,'must be an integer')
        else:
            self.__width = width

    
    def get_width(self):
        """
            Returns the width of rectangle object
        """
        return self.__width

    def set_height(self, height):
        """
            Sets the width of rectangle object

            Parameters
            ----------
            height: int
                height of the rectangle
        """
        if height <= 0:
            raise ValueError(height,'must be > 0')
        elif type(height) is not int:
            raise TypeError(height,'must be an integer')
        else:
            self.__height = height

    def get_height(self):
        """
            Returns the height of rectangle object
        """

        return self.__height

    def set_x(self, x):
        """
            Sets the x- position of rectangle object

            Parameters
            ----------
            x: int
                x-position of the rectangle
        """
        if x < 0:
            raise ValueError(x,'must be >= 0')
        elif type(x) is not int:
            raise TypeError(x,'must be an integer')
        else:
            self.__x = x

    def get_x(self):
        """
            Returns the height of rectangle object
        """
        return self.__x

    def set_y(self, y):
        """
            Sets the y-position of the rectangle object

            Parameters
            ----------
            y: int
                y-position of the rectangle
        """
        if y < 0:
            raise ValueError(y,'must be >= 0')
        elif type(y) is not int:
            raise TypeError(y,'must be an integer')
        self.__y = y

    def get_y(self):
        """
            Returns the y-position of rectangle object
        """
        return self.__y

    def area(self):
        """
            Returns the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
            Prints the rectangle instance with the character #
        """
        for y in range(self.get_y()):
            for x in range(self.get_x()):
                print('#')
            print('\n')

    def __str__(self):
        """
            Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.get_x(), self.get_y(), self.get_width(),
                                                       self.get_height())


