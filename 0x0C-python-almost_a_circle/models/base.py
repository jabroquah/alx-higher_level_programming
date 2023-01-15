#!/usr/bin/python3
"""Defines a base class for other classes in this project."""

class Base():
    """
        A base class
        ...

        Attributes
        ----------
        __nb_objects: int
            the number of objects

        Methods
        -------

    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        Parameters
        ----------
        id: int, optional
            id of instance object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects + 1
