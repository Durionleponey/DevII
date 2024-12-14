from math import gcd

class FractionError(Exception):
    pass


class Fraction(Exception):
    """Class representing a fraction and operations on it

    Author : Clarambaux Robin
    Date : November 2024
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        POST :
            -Creates a valid fraction in its reduced form based on the given numerator (num) and denominator (den).
        RAISES :

            -Raises FractionError if 'den' == 0.
            -Raises FractionError if 'den' and 'num' are not integer

        """

        if isinstance(num, int) and isinstance(den, int):
            pass
        else:
            raise FractionError("'den' and 'num' should be integer")

        if den == 0:
            raise FractionError("'den' can't be 0")

        common_divisor = gcd(num, den)
        self._num = num // common_divisor
        self._den = den // common_divisor

        if self._den < 0:
            self._den = -self._den
            self._num = -self._num



    @property
    def numerator(self):
        return self._num


    @property
    def denominator(self):
        return self._den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction


        POST :
            - Returns a string in the format "numerator/denominator"
        """
        return f"{self._num}/{self._den}"

    def as_mixed_number(self):
        """
        Return a textual representation of the fraction as a mixed number.

        POST :
            - Returns a string representing the fraction as an integer part and a proper fraction part.
            - The format is:
                - "X" if the fraction is an integer.
                - "X + Y/Z" if the fraction is positive and not an integer.
                - "X - Y/Z" if the fraction is negative and not an integer.
                - "0 + Y/Z" or "0 - Y/Z" if the fraction's absolute value is less than 1.
        """
        if self.numerator == 0:
            return "0"

        sign = '-' if self.numerator < 0 else ''
        a = abs(self.numerator)
        b = abs(self.denominator)
        integer_part = a // b
        fraction_part = a % b

        # Fraction propre
        if integer_part == 0:
            return f"0 {sign}+ {fraction_part}/{b}" if sign == '' else f"0 - {fraction_part}/{b}"

        # Pas de partie fractionnaire
        if fraction_part == 0:
            return f"{sign}{integer_part}"

        # Sinon, on affiche avec une partie entière et une partie fractionnaire
        if sign:
            return f"-{integer_part} - {fraction_part}/{b}"
        else:
            return f"{integer_part} + {fraction_part}/{b}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions


         POST :
         - Returns a new `Fraction` instance representing the sum of the two fractions.
         RAISES :
         - Raises FractionError if `other` is not an instance of `Fraction`.
         """
        if not isinstance(other, Fraction):
            raise FractionError("'other' must be an instance of `Fraction`")

        newNumerator = self.numerator*other.denominator + other.numerator*self.denominator
        newDenominator = self.denominator * other.denominator

        return Fraction(newNumerator, newDenominator)


    def __sub__(self, other):
        """Overloading of the - operator for fractions


        POST :
            - Returns a new `Fraction` instance representing the sustraction of the two fractions.
        RAISES :
            - Raises FractionError if `other` is not an instance of `Fraction`.

        """

        if not isinstance(other, Fraction):
            raise FractionError("'other' must be an instance of `Fraction`")

        newNumerator = self.numerator*other.denominator - other.numerator*self.denominator
        newDenominator = self.denominator * other.denominator

        return Fraction(newNumerator, newDenominator)



    def __mul__(self, other):
        """Overloading of the * operator for fractions


        POST :
             - Returns a new `Fraction` instance representing the product of the two fractions.
        RAISES :
             - Raises FractionError if `other` is not an instance of `Fraction`.
        """

        if not isinstance(other, Fraction):
            raise FractionError("'other' must be an instance of `Fraction`")

        newNumerator = self.numerator*other.numerator
        newDenominator = self.denominator * other.denominator

        return Fraction(newNumerator, newDenominator)



    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        POST :
            - Returns a new `Fraction` instance representing the division of the two fractions.
        RAISES :
            - Raises FractionError if:
            * `other` is not an instance of `Fraction`.
            * `other.numerator` is 0 (division by zero).

        """

        if not isinstance(other, Fraction):
            raise FractionError("'other' must be an instance of `Fraction`")

        othernumeratorInversed = other.denominator
        otherdenominatorInversed = other.numerator


        newNumerator = self.numerator*othernumeratorInversed
        newDenominator = self.denominator * otherdenominatorInversed

        return Fraction(newNumerator, newDenominator)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        POST :
        - Returns a new `Fraction` instance representing the fraction to the power of the other.
        RAISES :
        - Raises FractionError if `other` is not an instance of `Fraction`.
        """

        if not isinstance(other, int):
            raise FractionError("'other' must be a integer")

        newNumerator = self.numerator ** other
        newDenominator = self.denominator ** other


        return Fraction(newNumerator, newDenominator)


    def __eq__(self, other):
        """Overloading of the == operator for fractions


        POST :
        - Returns a Booleans representing if the two fractions are equal.
        RAISES :
        - Raises FractionError if `other` is not an instance of `Fraction`.

        """

        if not isinstance(other, Fraction):
            raise FractionError("'other' must be an instance of `Fraction`")

        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction

        POST : return the decimal value of the fraction
        """
        return self.numerator / self.denominator


    # ------------------ Properties checking  ------------------
    @property
    def is_zero(self):
        """Check if a fraction's value is 0

        POST : Boolean representing if the fraction is zero.
        """
        return self.numerator == 0

    @property
    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)


        POST :
             - Returns a Boolean indicating if the fraction is an integer.

        """
        return self.numerator % self.denominator == 0

    @property
    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        POST :
        -  Return abs(self.numerator) < abs(self.denominator)

        """
        return abs(self.numerator) < abs(self.denominator)

    @property
    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        POST :
            - Returns a Boolean indicating if the numerator is 1 in the reduced form.

        """
        return self.numerator == 1


    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction


        POST :
         - Returns a Boolean indicating if the two fractions are adjacent
        RAISES :
         - Raises FractionError if `other` is not an instance of `Fraction`.

        """
        if not isinstance(other, Fraction):
            raise FractionError("'other' must be an instance of `Fraction`")

        difference = self - other

        return abs(difference.numerator) == 1 and difference.denominator > 0

if __name__ == '__main__':
    #frac1 = Fraction(1, 1)
    #print(frac1)
    #print(frac1.as_mixed_number())
    #frac2 = Fraction(1, 2)
    #print(frac1.is_adjacent_to(frac2))
    #
    #frac3 = Fraction(1, 4)
    #
    #print(frac1-frac3)

    frac = Fraction(4, 2)
    print(frac.as_mixed_number())
