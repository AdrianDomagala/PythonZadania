import unittest
from math import pi
import numpy as np


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self):  # zwraca string "Point(x, y)"
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):  # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny (liczba)
        return Point(self.x * other.x, self.y * other.y)

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return pow(self.x ** 2 + self.y ** 2, 0.5)

    def distance_to_other(self, other):
        return pow((self.x - other.x) ** 2 + (self.y - other.y) ** 2, 0.5)

    def middle(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Promień ujemny!")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, radius = {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):  # pole powierzchni
        return pi * self.radius ** 2

    def move(self, x, y):  # przesuniecie o (x, y)
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)


class TestFrac(unittest.TestCase):

    def test_cmp(self):
        self.assertTrue(Circle(1, 1, 2) == Circle(1, 1, 2))
        self.assertFalse(Circle(3, 5, 1) == Circle(5, 3, 1))
        self.assertFalse(Circle(3, 5, 1) == Circle(3, 5, 2))
        self.assertFalse(Circle(-3, 15, 5) != Circle(-3, 15, 5))

    def test_area(self):
        self.assertEqual(Circle(2, 5, 5).area(), pi * 5 ** 2)
        self.assertEqual(Circle(-2, -3, 3).area(), pi * 3 ** 2)
        self.assertEqual(Circle(1, 6, 10).area(), Circle(-5, 3, 10).area())

    def test_move(self):
        self.assertTrue(Circle(1, 6, 10).move(1, 2) == Circle(2, 8, 10))
        self.assertTrue(Circle(1, 6, 10).move(-3, 6) == Circle(-2, 12, 10))


if __name__ == '__main__':
    unittest.main()