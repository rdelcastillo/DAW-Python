"""
Test Clase Date
"""
from ej05poo.tanda2.ej09_date import Date
import unittest

class TestDate(unittest.TestCase):
    date1 = Date(1, 2, 2023)
    date2 = Date(28, 2, 2022)

    def test_date(self):
        new_date = Date(self.date1)
        self.assertEqual(new_date, self.date1)
        self.assertRaises(ValueError, Date, -1, 1, 1)
        self.assertRaises(ValueError, Date, 29, 2, 2023)
        self.assertRaises(ValueError, Date, 31, 6, 2023)
        self.assertRaises(TypeError, Date, 2, "La cagaste Burt Lancaster", 2022)
        self.assertRaises(TypeError, Date, 2, 5)

    def test_day(self):
        with self.assertRaises(ValueError):
            TestDate.date1.day = 0
        with self.assertRaises(ValueError):
            TestDate.date2.day = 29

    def test_month(self):
        with self.assertRaises(ValueError):
            TestDate.date1.month = 0
        with self.assertRaises(ValueError):
            TestDate.date2.day = -13

    def test_year(self):
        with self.assertRaises(ValueError):
            TestDate.date1.year = 0
        with self.assertRaises(ValueError):
            TestDate.date2.year = -13

    def test_str(self):
        self.assertEqual(str(self.date1), "1 de Febrero de 2023")
        self.assertEqual(str(self.date2), "28 de Febrero de 2022")

    def test_is_leap(self):
        self.assertFalse(self.date1.is_leap())
        self.assertFalse(self.date2.is_leap())
        new_date1 = Date(1, 1, 2000)
        new_date2 = Date(1, 1, 2004)
        new_date3 = Date(1, 1, 2100)
        self.assertTrue(new_date1.is_leap())
        self.assertTrue(new_date2.is_leap())
        self.assertFalse(new_date3.is_leap())

    def test_add(self):
        self.assertEqual(self.date1 + 1000, Date(28, 10, 2025))
        self.assertEqual(self.date2 + 3000, Date(17, 5, 2030))

    def test_subtract(self):
        self.assertEqual(Date(28, 10, 2025) - 1000, self.date1)
        self.assertEqual(Date(17, 5, 2030) - 3000, self.date2)

    @unittest.skip("Tarda mucho")
    def test_day_of_week(self):
        self.assertEqual(Date(21, 2, 2023).day_of_week(), 1)
        self.assertEqual(Date(19, 2, 2023).day_of_week(), 6)

    def test_compare(self):
        self.assertGreater(self.date1, self.date2)
        self.assertGreaterEqual(self.date1, self.date2)
        self.assertNotEqual(self.date1, self.date2)
        self.assertFalse(self.date1 < self.date2)
        self.assertFalse(self.date1 <= self.date2)


if __name__ == '__main__':
   unittest.main()