#!/usr/bin/python3
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
    def display(self):#NEEDS TO BE UPDATED [TASK7]
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
        return self.width
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
    def update(self, *args, **kwargs)
        
