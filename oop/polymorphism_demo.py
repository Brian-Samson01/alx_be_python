import math


class Shape:
    def area(self):
        """
        Base method to be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides Shape.area() to calculate rectangle area.
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Circle with radius.
        """
        self.radius = radius

    def area(self):
        """
        Overrides Shape.area() to calculate circle area.
        """
        return math.pi * (self.radius ** 2)
