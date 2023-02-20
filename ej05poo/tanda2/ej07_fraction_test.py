"""
Test Clase Fraction
"""
from ej07_fraction import Fraction
import unittest

class TestFraction(unittest.TestCase):
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)

    def test_fraction(self):
        f3 = Fraction(2, 5)
        self.assertEquals("2/5", str(f3))
        f4 = Fraction(4, 10)  # fracción que debe simplificarse
        self.assertEquals(2, f4.num)
        self.assertEquals(5, f4.den)
        with self.assertRaises(ZeroDivisionError):  # ¿lanza excepción con denominador cero?
            Fraction(1, 0)

    def test_get_num(self):
        self.assertEquals(1, self.f1.num)
        self.assertEquals(2, self.f2.num)

    def test_get_den(self):
        self.assertEquals(2, self.f1.den)
        self.assertEquals(3, self.f2.den)

    def test_to_str(self):
        self.assertEquals("1/2", str(self.f1))
        self.assertEquals("2/3", str(self.f2))

    def test_compare_to(self):
        self.assertTrue(self.f1 < self.f2)
        self.assertTrue(self.f1 <= self.f2)
        self.assertTrue(self.f1 != self.f2)
        self.assertFalse(self.f1 > self.f2)
        self.assertFalse(self.f1 >= self.f2)
        self.assertFalse(self.f1 == self.f2)

    def test_result(self):
        self.assertEquals(0.5, self.f1.result())

    def test_multiply_int(self):
        f3 = self.f1 * 2
        f4 = Fraction(1, 1)
        self.assertTrue(f3 == f4)

    def test_multiply_fraction(self):
        f3 = self.f1 * self.f2
        self.assertEquals(Fraction(1, 3), f3)

    def test_divide(self):
        f3 = self.f1 / self.f2
        self.assertEquals(Fraction(3, 4), f3)

    def test_add(self):
        f3 = self.f1 + self.f2
        self.assertEquals(Fraction(7, 6), f3)

    def test_subtract(self):
        f3 = self.f1 - self.f2
        self.assertEquals(Fraction(-1, 6), f3)


if __name__ == '__main__':
   unittest.main()