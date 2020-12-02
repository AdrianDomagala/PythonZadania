import unittest


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

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.

class TestPoint(unittest.TestCase):

    def test_cmp(self):
        self.assertTrue(Point(1, 1) == Point(1, 1))
        self.assertFalse(Point(1, 5) == Point(5, 1))
        self.assertFalse(Point(-1, -2) != Point(-1, -2))

    def test_vector_operation(self):
        # +
        self.assertEqual(Point(0, 0) + Point(2, 2), Point(2, 2))
        self.assertEqual(Point(-2, -1) + Point(2, 2), Point(0, 1))
        self.assertEqual(Point(0, 0) + Point(-2, 2), Point(-2, 2))
        # -
        self.assertEqual(Point(0, 0) - Point(2, 2), Point(-2, -2))
        self.assertEqual(Point(-2, -1) - Point(2, 2), Point(-4, -3))
        self.assertEqual(Point(0, 0) - Point(-2, 2), Point(2, -2))
        # *
        self.assertEqual(Point(0, 0) * Point(2, 2), Point(0, 0))
        self.assertEqual(Point(-2, -1) * Point(2, 2), Point(-4, -2))
        self.assertEqual(Point(2, -3) * Point(-2, 2), Point(-4, -6))
        # cross
        self.assertEqual(Point(1, 2).cross(Point(2, 3)), -1)
        self.assertEqual(Point(1, 2).cross(Point(-1, 3)), 5)
        # len
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(6, 8).length(), 10)

    def test_print(self):
        self.assertEqual(Point(1, 2).__str__(), '(1, 2)')
        self.assertEqual(Point(1, 2).__repr__(), 'Point(1, 2)')


if __name__ == "__main__":
    unittest.main()
