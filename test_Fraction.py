import unittest
from Fraction import Fraction, FractionError

class TestFraction(unittest.TestCase):

    def test_constructor_valid(self):
        frac = Fraction(3, 4)
        self.assertEqual(frac.numerator, 3)
        self.assertEqual(frac.denominator, 4)

    def test_constructor_invalid_den_zero(self):
        with self.assertRaises(FractionError):
            Fraction(1, 0)



    def test_str(self):
        frac = Fraction(3, 4)
        self.assertEqual(str(frac), "3/4")

    def test_as_mixed_number(self):
        frac = Fraction(7, 3)
        self.assertEqual(frac.as_mixed_number(), "2 + 1/3")




    def test_add(self):
        frac1 = Fraction(1, 3)
        frac2 = Fraction(2, 3)
        result = frac1 + frac2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    def test_sub(self):
        frac1 = Fraction(1, 3)
        frac2 = Fraction(2, 3)
        result = frac1 - frac2
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 3)

        frac3 = Fraction(1, 3)
        frac4 = Fraction(1, 2)
        result = frac3 - frac4

    def test_truediv(self):
        frac1 = Fraction(3, 4)
        frac2 = Fraction(2, 5)
        result = frac1 / frac2
        self.assertEqual(result.numerator, 15)
        self.assertEqual(result.denominator, 8)


    def test_eq(self):
        frac1 = Fraction(2, 3)
        frac2 = Fraction(4, 6)
        self.assertTrue(frac1 == frac2)

        frac3 = Fraction(1, 2)
        self.assertFalse(frac1 == frac3)




    def test_is_integer(self):
        frac = Fraction(4, 2)
        self.assertTrue(frac.is_integer)

        frac = Fraction(3, 2)
        self.assertFalse(frac.is_integer)

    def test_is_proper(self):
        frac = Fraction(3, 4)
        self.assertTrue(frac.is_proper)

        frac = Fraction(5, 4)
        self.assertFalse(frac.is_proper)

    def test_is_adjacent_to(self):
        frac1 = Fraction(1, 3)
        frac2 = Fraction(1, 2)
        self.assertTrue(frac1.is_adjacent_to(frac2))

        frac3 = Fraction(1, 4)
        self.assertTrue(frac1.is_adjacent_to(frac3))


if __name__ == "__main__":
    unittest.main()
