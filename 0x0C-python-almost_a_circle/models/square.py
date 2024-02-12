#!/usr/bin/python3
"""Defining a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns the str & print of a Square."""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    def display(self):
        """Prints the Square with the '#' symbol"""
        if self.width == 0 or self.height == 0:
            print("")
        for _ in range(self.y):
            print()
        for _ in range(self.size):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Getter & setter for the square's Side value"""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Udates the Square values"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionay Represntation of a square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
