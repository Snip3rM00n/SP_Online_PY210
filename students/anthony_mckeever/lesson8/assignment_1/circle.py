"""
Programming In Python - Lesson 8 Assignment 1: Circles
Code Poet: Anthony McKeever
Start Date: 09/05/2019
End Date: 09/05/2019
"""

import math
import operator


class Circle():
    """
    An object representing a circle.
    """
    def __init__(self, radius):
        self.radius = radius

    
    @property
    def diameter(self):
        return self.radius * 2


    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)


    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter / 2)
        return self


    def __str__(self):
        return f"Circle with radius: {self.radius}"


    def __repr__(self):
        return f"Circle({self.radius})"


    def __add__(self, other):
        return Circle(self.radius + other.radius)

    
    def __iadd__(self, other):
        return self.__add__(other)

    
    def __sub__(self, other):
        return Circle(self.radius - other)

    
    def __isub__(self, other):
        return self.__sub__(other)


    def __mul__(self, other):
        return Circle(self.radius * other)


    def __imul__(self, other):
        return self.__mul__(other)


    def __rmul__(self, other):
        return Circle(self.radius * other)


    def __lt__(self, other):
        return (self.radius, self.diameter, self.area) < (other.radius, other.diameter, other.area)

    
    def __eq__(self, other):
        return (self.radius, self.diameter, self.area) == (other.radius, other.diameter, other.area)

    
    def __truediv__(self, other):
        return Circle(self.radius / other.radius)


    def __floordiv__(self, other):
        return Circle(self.radius // other.radius)
