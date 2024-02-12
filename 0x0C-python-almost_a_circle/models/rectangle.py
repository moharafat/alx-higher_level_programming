#!/usr/bin/python3
"""Rectangle is a class tha inherites from Base class"""
from models.base import Base


class Rectangle(Base):
    """ Creating a new class called Rectangle and its attributes are:
    width: which is the width of the rectangle
    height: which is the length of i
    x: how far away the rectangle is from the left Y-axis
    y: how far away the rectangle is from the top x-axis[newlines]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Setter & getter the Rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Setter & getter the Rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Setter & getter the Rectangle's x-axis coordiante."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Setter & getter the Rectangle's y-axis coordiante."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints the Rectangle with the '#' symbol"""
        if self.width == 0 or self.height == 0:
            print("")
        for _ in range(self.y):  # Print new lines for y coordinate
            print()
        for _ in range(self.height):  # Iterate over rows
            for _ in range(self.x):  # Print spaces for x coordinate
                print(" ", end="")
            for _ in range(self.width):  # Print # for width of the rectangle
                print("#", end="")
            print()

    def __str__(self):
        """Returns the str represrntation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
    .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the rectangle with new values"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionaryy representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
