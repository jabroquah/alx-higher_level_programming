#!/usr/bin/python3
"""
    A model for a square
"""


from rectangle import Rectangle
class Square(Rectangle):
    """
        A square class
        ...

        Methods
        -------

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Parameters
            ----------
            size: int
                width and height is assigned to size
            x: int
                x-position of the square
            y: int
                y-position of the square
            id: int, optional
                id of the square instance object

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            Returns [Square] (<id>) <x>/<y> - <size>
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.get_x(), self.get_y(), self.get_width())