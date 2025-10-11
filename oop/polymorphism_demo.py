# polymorphism_demo.py

import math

# Base Class
class Shape:
    def area(self):
        """Base method for calculating area — must be overridden by subclasses"""
        raise NotImplementedError("Subclasses must override the area() method.")


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize rectangle dimensions"""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.length * self.width


# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize circle radius"""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * (self.radius ** 2)
