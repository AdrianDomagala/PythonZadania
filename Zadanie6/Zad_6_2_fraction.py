import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return f'{self.x}'
        return f'{self.x}/{self.y}'

    def __repr__(self):  # zwraca "Frac(x, y)"
        return f'Frac({self.x}, {self.y})'

    # nwd
    def nwd(self):
        a = self.x
        b = self.y
        while b:
            a, b = b, a % b
        return a

    def shortening(self):
        nwd_s = self.nwd()
        return Frac(self.x / nwd_s, self.y / nwd_s)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        f1 = Frac(self.x * other.y, self.y * other.y)
        f2 = Frac(other.x * self.y, self.y * other.y)
        return f1.x == f2.x

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        f1 = Frac(self.x * other.y, self.y * other.y)
        f2 = Frac(other.x * self.y, self.y * other.y)
        return f1.x < f2.x

    def __le__(self, other):
        f1 = Frac(self.x * other.y, self.y * other.y)
        f2 = Frac(other.x * self.y, self.y * other.y)
        return f1.x <= f2.x

    #arithmetical operation
    def __add__(self, other):  # frac1 + frac2
        f1 = Frac(self.x * other.y, self.y * other.y)
        f2 = Frac(other.x * self.y, self.y * other.y)
        return Frac(f1.x + f2.x, f1.y).shortening()

    def __sub__(self, other):  # frac1 - frac2
        f1 = Frac(self.x * other.y, self.y * other.y)
        f2 = Frac(other.x * self.y, self.y * other.y)
        return Frac(f1.x - f2.x, f1.y).shortening()

    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y).shortening()

    def __truediv__(self, other):  # frac1 / frac2, Python 3
        return Frac(self.x * other.y, self.y * other.x).shortening()

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))  # immutable fracs


# Kod testujący moduł.

class TestFrac(unittest.TestCase):

    def test_cmp(self):
        self.assertTrue(Frac(1, 1) == Frac(1, 1))
        self.assertFalse(Frac(3, 5) == Frac(5, 3))
        self.assertFalse(Frac(-3, 15) != Frac(-3, 15))

        self.assertTrue(Frac(23, 12) <= Frac(23, 12))
        self.assertTrue(Frac(23, 12) <= Frac(23, 2))
        self.assertFalse(Frac(3, 5) > Frac(5, 3))
        self.assertFalse(Frac(-3, 15) < Frac(-3, 15))

    def test_shortening(self):
        self.assertEqual(Frac(14, 70).shortening(), Frac(1, 5))
        self.assertEqual(Frac(-2, 8).shortening(), Frac(-1, 4))

    def test_unary_operator(self):
        self.assertEqual(Frac(3, 5).__pos__(), Frac(3, 5))
        self.assertEqual(Frac(-2, -1).__neg__(), Frac(2, -1))
        self.assertEqual(-Frac(-2, -1), Frac(2, -1))
        self.assertEqual(Frac(-5, 2).__invert__(), Frac(2, -5))
        self.assertEqual(float(Frac(1, 4)), 0.25)

    def test_arithmetical_operation(self):
        #+
        self.assertEqual(Frac(1, 2) + Frac(1, 4), Frac(3, 4))
        self.assertEqual(Frac(3, 8) + Frac(2, 2), Frac(11, 8))
        self.assertEqual(Frac(0, 1) + Frac(1, 2), Frac(1, 2))
        #-
        self.assertEqual(Frac(1, 2) - Frac(1, 4), Frac(1, 4))
        self.assertEqual(Frac(3, 8) - Frac(2, 2), Frac(-5, 8))
        self.assertEqual(Frac(0, 1) - Frac(1, 2), Frac(-1, 2))
        #*
        self.assertEqual(Frac(1, 2) * Frac(1, 4), Frac(1, 8))
        self.assertEqual(Frac(3, -8) * Frac(2, 2), Frac(6, -16))
        self.assertEqual(Frac(0, 1) * Frac(1, 2), Frac(0, 2))
        #/
        self.assertEqual(Frac(1, 2) / Frac(1, 4), Frac(2, 1))
        self.assertEqual(Frac(3, -8) / Frac(2, 3), Frac(9, -16))
        self.assertEqual(Frac(0, 1) / Frac(1, 2), Frac(0, 2))


if __name__ == '__main__':
    unittest.main()
