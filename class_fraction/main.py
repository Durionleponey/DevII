from Fraction import Fraction

frac1 = Fraction(1, 3)
frac2 = Fraction(1, 2)
frac3 = Fraction(1, 4)
frac4 = Fraction(4, 2)

print(frac1)
print(frac2)
print(frac3)
print(frac4)

print(frac1.is_adjacent_to(frac2))
print(frac1.is_adjacent_to(frac3))

print(frac1 - frac3)
print(frac1 + frac2)
print(frac1 * frac2)
print(frac2 / frac1)
print(frac1 ** 2)

print(frac1 == frac2)
print(frac4.is_integer)
print(frac1.is_integer)
print(frac1.is_proper)
print(frac1.is_unit)
print(float(frac1))
print(frac1.as_mixed_number())
