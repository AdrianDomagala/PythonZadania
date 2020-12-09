import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError('The denominator cannot be zero!')
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
        return Frac(int(self.x / nwd_s), int(self.y / nwd_s))

    @staticmethod
    def frac_from_float(f):
        x, y = f.as_integer_ratio()
        return Frac(x, y)

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

    # arithmetical operation
    def __add__(self, other):  # frac1 + frac2
        if isinstance(other, int):
            return Frac(self.x + self.y * other, self.y).shortening()
        elif isinstance(other, float):
            other = Frac.frac_from_float(other)
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y).shortening()

    __radd__ = __add__

    def __sub__(self, other):  # frac1 - frac2
        if isinstance(other, int):
            return Frac(self.x - self.y * other, self.y).shortening()
        elif isinstance(other, float):
            other = Frac.frac_from_float(other)
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y).shortening()

    def __rsub__(self, other):  # int-frac
        if isinstance(other, float):
            return Frac.frac_from_float(other) - self
        return Frac(self.y * other - self.x, self.y).shortening()

    def __mul__(self, other):  # frac1 * frac2
        if isinstance(other, int):
            return Frac(self.x * other, self.y).shortening()
        elif isinstance(other, float):
            other = Frac.frac_from_float(other)
        return Frac(self.x * other.x, self.y * other.y).shortening()

    __rmul__ = __mul__

    def __truediv__(self, other):  # frac1 / frac2, Python 3
        if isinstance(other, int):
            if other == 0:
                raise ValueError('Cannot divide by zero!')
            return Frac(self.x, self.y * other).shortening()
        elif isinstance(other, float):
            other = Frac.frac_from_float(other)
        return Frac(self.x * other.y, self.y * other.x).shortening()

    def __rtruediv__(self, other):
        if isinstance(other, float):
            return Frac.frac_from_float(other) / self
        return Frac(other * self.y, self.x)

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
        # +
        self.assertEqual(Frac(1, 2) + Frac(1, 4), Frac(3, 4))
        self.assertEqual(Frac(3, 8) + Frac(2, 2), Frac(11, 8))
        self.assertEqual(Frac(0, 1) + Frac(1, 2), Frac(1, 2))
        # -
        self.assertEqual(Frac(1, 2) - Frac(1, 4), Frac(1, 4))
        self.assertEqual(Frac(3, 8) - Frac(2, 2), Frac(-5, 8))
        self.assertEqual(Frac(0, 1) - Frac(1, 2), Frac(-1, 2))
        # *
        self.assertEqual(Frac(1, 2) * Frac(1, 4), Frac(1, 8))
        self.assertEqual(Frac(3, -8) * Frac(2, 2), Frac(6, -16))
        self.assertEqual(Frac(0, 1) * Frac(1, 2), Frac(0, 2))
        # /
        self.assertEqual(Frac(1, 2) / Frac(1, 4), Frac(2, 1))
        self.assertEqual(Frac(3, -8) / Frac(2, 3), Frac(9, -16))
        self.assertEqual(Frac(0, 1) / Frac(1, 2), Frac(0, 2))

    def test_arithmetical_operation_frac_int(self):
        # +
        self.assertEqual(Frac(1, 2) + 2, Frac(5, 2))
        self.assertEqual(Frac(3, 8) + -4, Frac(-29, 8))
        self.assertEqual(Frac(-3, 3) + -1, Frac(-2, 1))
        # -
        self.assertEqual(Frac(1, 2) - 2, Frac(-3, 2))
        self.assertEqual(Frac(3, 8) - -4, Frac(35, 8))
        self.assertEqual(Frac(-3, 3) - -1, Frac(0, 1))
        # *
        self.assertEqual(Frac(1, 2) * 2, Frac(1, 1))
        self.assertEqual(Frac(3, 8) * -4, Frac(-3, 2))
        self.assertEqual(Frac(-3, 3) * -1, Frac(1, 1))
        # /
        self.assertEqual(Frac(1, 2) / 2, Frac(1, 4))
        self.assertEqual(Frac(3, 8) / -4, Frac(-3, 32))
        self.assertEqual(Frac(-3, 3) / 2, Frac(-1, 2))

    def test_arithmetical_operation_int_frac(self):
        # +
        self.assertEqual(2 + Frac(1, 2), Frac(5, 2))
        self.assertEqual(-4 + Frac(3, 8), Frac(-29, 8))
        self.assertEqual(-1 + Frac(-3, 3), Frac(-2, 1))
        # -
        self.assertEqual(2 - Frac(1, 2), Frac(3, 2))
        self.assertEqual(-4 - Frac(3, 8), Frac(-35, 8))
        self.assertEqual(-1 - Frac(-3, 3), Frac(0, 1))
        # *
        self.assertEqual(2 * Frac(1, 2), Frac(1, 1))
        self.assertEqual(-4 * Frac(3, 8), Frac(-3, 2))
        self.assertEqual(-1 * Frac(-3, 3), Frac(1, 1))
        # /
        self.assertEqual(2 / Frac(1, 2), Frac(4, 1))
        self.assertEqual(-4 / Frac(3, 8), Frac(-32, 3))
        self.assertEqual(3 / Frac(-3, 3), Frac(-3, 1))


if __name__ == '__main__':
    unittest.main()