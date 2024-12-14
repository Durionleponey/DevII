import unittest
from Fraction import Fraction, FractionError
#utilisation de chatgpt dans ce fichier test_Fraction

class TestFraction(unittest.TestCase):

    # --- Tests pour le constructeur ---
    def test_constructor_valid(self):
        frac = Fraction(3, 4)
        self.assertEqual(frac.numerator, 3)
        self.assertEqual(frac.denominator, 4)

    def test_constructor_negative(self):
        frac = Fraction(-3, 4)
        self.assertEqual(frac.numerator, -3)
        self.assertEqual(frac.denominator, 4)

        frac = Fraction(3, -4)
        self.assertEqual(frac.numerator, -3)
        self.assertEqual(frac.denominator, 4)

        frac = Fraction(-3, -4)
        self.assertEqual(frac.numerator, 3)
        self.assertEqual(frac.denominator, 4)

    def test_constructor_invalid_den_zero(self):
        with self.assertRaises(FractionError):#with sert à voir si une exception est levée
            Fraction(1, 0)

    # --- Tests pour la méthode __str__ ---
    def test_str(self):
        frac = Fraction(3, 4)
        self.assertEqual(str(frac), "3/4")

        frac = Fraction(6, 8)
        self.assertEqual(str(frac), "3/4")  # Réduction automatique

    # --- Tests pour as_mixed_number ---
    def test_as_mixed_number(self):
        #Fraction propre positive
        frac = Fraction(2, 3)
        self.assertEqual(frac.as_mixed_number(), "0 + 2/3")

        #Fraction propre négative
        frac = Fraction(-2, 3)
        self.assertEqual(frac.as_mixed_number(), "0 - 2/3")

        #Fraction impropre positive
        frac = Fraction(7, 3)
        self.assertEqual(frac.as_mixed_number(), "2 + 1/3")

        #Fraction impropre négative
        frac = Fraction(-7, 3)
        self.assertEqual(frac.as_mixed_number(), "-2 - 1/3")

        #Fraction nulle
        frac = Fraction(0, 5)
        self.assertEqual(frac.as_mixed_number(), "0")

        #Fraction entière positive
        frac = Fraction(4, 2)
        self.assertEqual(frac.as_mixed_number(), "2")

        #Fraction entière négative
        frac = Fraction(-4, 2)
        self.assertEqual(frac.as_mixed_number(), "-2")

        #Fraction impropre avec un dénominateur négatif
        frac = Fraction(5, -3)
        self.assertEqual(frac.as_mixed_number(), "-1 - 2/3")

        #Fraction propre avec un numérateur négatif
        frac = Fraction(-1, 4)
        self.assertEqual(frac.as_mixed_number(), "0 - 1/4")

        #Fraction réduite mais impropre
        frac = Fraction(9, 6)  # Équivaut à 3/2
        self.assertEqual(frac.as_mixed_number(), "1 + 1/2")

        #Fraction réduite avec une partie fractionnaire nulle
        frac = Fraction(6, 3)  # Équivaut à 2
        self.assertEqual(frac.as_mixed_number(), "2")

        #Fraction négative avec un dénominateur négatif
        frac = Fraction(-10, -3)  # Équivaut à 10/3
        self.assertEqual(frac.as_mixed_number(), "3 + 1/3")

    # --- Tests pour l'addition ---
    def test_add(self):
        # Cas simple : deux fractions positives
        frac1 = Fraction(1, 3)
        frac2 = Fraction(2, 3)
        result = frac1 + frac2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

        # Avec une fraction nulle
        frac3 = Fraction(0, 1)
        result = frac1 + frac3
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

        # Avec une fraction négative
        frac4 = Fraction(-1, 3)
        result = frac1 + frac4
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

        # Avec deux fractions négatives
        frac5 = Fraction(-1, 3)
        frac6 = Fraction(-2, 3)
        result = frac5 + frac6
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 1)

        # Avec une fraction positive et une fraction négative
        frac7 = Fraction(5, 6)
        frac8 = Fraction(-1, 2)
        result = frac7 + frac8
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

        # Avec des fractions impropres
        frac9 = Fraction(7, 3)
        frac10 = Fraction(5, 2)
        result = frac9 + frac10
        self.assertEqual(result.numerator, 29)
        self.assertEqual(result.denominator, 6)

        # Avec une fraction impropre et une fraction négative
        frac11 = Fraction(7, 3)
        frac12 = Fraction(-2, 3)
        result = frac11 + frac12
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 3)

        # Avec réduction automatique
        frac13 = Fraction(3, 6)
        frac14 = Fraction(1, 6)
        result = frac13 + frac14
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 3)

        # Avec réduction automatique et fractions négatives
        frac15 = Fraction(-3, 6)
        frac16 = Fraction(1, 6)
        result = frac15 + frac16
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 3)

    # --- Tests pour la soustraction ---
    def test_sub(self):
        # Cas simple : soustraction de deux fractions positives
        frac1 = Fraction(1, 3)
        frac2 = Fraction(2, 3)
        result = frac1 - frac2
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 3)

        # Soustraction de fractions avec des dénominateurs différents
        frac3 = Fraction(1, 2)
        frac4 = Fraction(1, 4)
        result = frac3 - frac4
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

        # Soustraction avec une fraction négative
        frac5 = Fraction(-1, 3)
        result = frac1 - frac5
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 3)

        # Soustraction entre deux fractions négatives
        frac6 = Fraction(-1, 2)
        frac7 = Fraction(-1, 4)
        result = frac6 - frac7
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 4)

        # Soustraction entre une fraction négative et une fraction positive
        frac8 = Fraction(-3, 4)
        frac9 = Fraction(1, 4)
        result = frac8 - frac9
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 1)

        # Soustraction entre des fractions impropres
        frac10 = Fraction(7, 3)
        frac11 = Fraction(5, 2)
        result = frac10 - frac11
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 6)

        # Soustraction avec réduction automatique
        frac12 = Fraction(3, 6)
        frac13 = Fraction(1, 6)
        result = frac12 - frac13
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

        # Soustraction avec une fraction nulle
        frac14 = Fraction(0, 1)
        result = frac1 - frac14
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

        # Soustraction d'une fraction positive par une fraction nulle
        result = frac14 - frac1
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 3)

    # --- Tests pour la multiplication ---
    def test_mul(self):
        # Cas simple : multiplication de deux fractions positives
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        result = frac1 * frac2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

        # Multiplication avec une fraction nulle
        frac3 = Fraction(0, 1)
        result = frac1 * frac3
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

        # Multiplication avec des fractions négatives
        frac4 = Fraction(-1, 2)
        result = frac1 * frac4
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 4)

        # Multiplication de deux fractions négatives
        frac5 = Fraction(-1, 3)
        frac6 = Fraction(-3, 4)
        result = frac5 * frac6
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

        # Multiplication d'une fraction positive avec une fraction négative
        frac7 = Fraction(3, 5)
        frac8 = Fraction(-2, 3)
        result = frac7 * frac8
        self.assertEqual(result.numerator, -2)
        self.assertEqual(result.denominator, 5)

        # Multiplication de fractions impropres
        frac9 = Fraction(7, 3)
        frac10 = Fraction(5, 2)
        result = frac9 * frac10
        self.assertEqual(result.numerator, 35)
        self.assertEqual(result.denominator, 6)

        # Multiplication avec réduction automatique
        frac11 = Fraction(3, 6)  # Réduit à 1/2
        frac12 = Fraction(2, 4)  # Réduit à 1/2
        result = frac11 * frac12
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

        # Multiplication avec une fraction unitaire
        frac13 = Fraction(1, 1)
        result = frac1 * frac13
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

        # Multiplication de fractions où une seule partie est négative
        frac14 = Fraction(-3, 5)
        frac15 = Fraction(4, 7)
        result = frac14 * frac15
        self.assertEqual(result.numerator, -12)
        self.assertEqual(result.denominator, 35)

    # --- Tests pour la division ---
    def test_truediv(self):
        # Division simple entre fractions positives
        frac1 = Fraction(3, 4)
        frac2 = Fraction(2, 5)
        result = frac1 / frac2
        self.assertEqual(result.numerator, 15)
        self.assertEqual(result.denominator, 8)

        # Division par une fraction négative
        frac3 = Fraction(-2, 5)
        result = frac1 / frac3
        self.assertEqual(result.numerator, -15)
        self.assertEqual(result.denominator, 8)

        # Division entre deux fractions négatives
        frac4 = Fraction(-3, 4)
        frac5 = Fraction(-2, 5)
        result = frac4 / frac5
        self.assertEqual(result.numerator, 15)
        self.assertEqual(result.denominator, 8)

        # Division par une fraction unitaire (ne change pas la valeur)
        frac6 = Fraction(1, 1)
        result = frac1 / frac6
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)

        # Division d'une fraction unitaire par une autre
        frac7 = Fraction(1, 1)
        frac8 = Fraction(3, 4)
        result = frac7 / frac8
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 3)

        # Division par une fraction impropre
        frac9 = Fraction(5, 3)
        frac10 = Fraction(7, 2)
        result = frac9 / frac10
        self.assertEqual(result.numerator, 10)
        self.assertEqual(result.denominator, 21)

        # Division d'une fraction par elle-même (doit donner 1/1)
        frac11 = Fraction(7, 3)
        result = frac11 / frac11
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

        # Division par une fraction nulle (doit lever une exception)
        frac12 = Fraction(0, 1)
        with self.assertRaises(FractionError):
            frac1 / frac12

        # Division d'une fraction nulle par une autre (doit donner 0)
        frac13 = Fraction(0, 1)
        frac14 = Fraction(2, 3)
        result = frac13 / frac14
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

        # Division avec réduction automatique
        frac15 = Fraction(6, 8)  # Réduit à 3/4
        frac16 = Fraction(9, 12)  # Réduit à 3/4
        result = frac15 / frac16
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

        # Division avec des signes mixtes
        frac17 = Fraction(3, 4)
        frac18 = Fraction(-2, 3)
        result = frac17 / frac18
        self.assertEqual(result.numerator, -9)
        self.assertEqual(result.denominator, 8)

    # --- Tests pour __eq__ ---
    def test_eq(self):
        # Égalité entre fractions équivalentes
        frac1 = Fraction(2, 3)
        frac2 = Fraction(4, 6)
        self.assertTrue(frac1 == frac2)

        # Inégalité entre deux fractions différentes
        frac3 = Fraction(1, 2)
        self.assertFalse(frac1 == frac3)

        # Égalité entre deux fractions identiques
        frac4 = Fraction(1, 3)
        frac5 = Fraction(1, 3)
        self.assertTrue(frac4 == frac5)

        # Égalité entre fractions réduites
        frac6 = Fraction(6, 9)  # Réduit à 2/3
        frac7 = Fraction(2, 3)
        self.assertTrue(frac6 == frac7)

        # Inégalité entre fractions impropres
        frac8 = Fraction(7, 3)
        frac9 = Fraction(5, 2)
        self.assertFalse(frac8 == frac9)

        # Égalité avec des fractions négatives
        frac10 = Fraction(-3, 4)
        frac11 = Fraction(3, -4)
        self.assertTrue(frac10 == frac11)

        # Inégalité entre fractions avec signes opposés
        frac12 = Fraction(3, 4)
        frac13 = Fraction(-3, 4)
        self.assertFalse(frac12 == frac13)

        # Égalité avec une fraction nulle
        frac14 = Fraction(0, 1)
        frac15 = Fraction(0, 5)
        self.assertTrue(frac14 == frac15)

        # Inégalité avec une fraction nulle et une fraction non nulle
        frac16 = Fraction(1, 3)
        self.assertFalse(frac14 == frac16)

        # Comparaison avec un autre type (doit lever une exception)
        with self.assertRaises(FractionError):
            frac1 == "2/3"

    # --- Tests pour les propriétés ---
    def test_is_integer(self):
        def test_is_integer(self):
            # Fraction réduite qui est un entier
            frac = Fraction(4, 2)  # Équivaut à 2
            self.assertTrue(frac.is_integer)

            # Fraction réduite qui n'est pas un entier
            frac = Fraction(3, 2)  # Équivaut à 1.5
            self.assertFalse(frac.is_integer)

            # Fraction déjà entière (numérateur multiple du dénominateur)
            frac = Fraction(6, 3)  # Équivaut à 2
            self.assertTrue(frac.is_integer)

            # Fraction nulle (0 est toujours un entier)
            frac = Fraction(0, 5)  # Équivaut à 0
            self.assertTrue(frac.is_integer)

            # Fraction négative entière
            frac = Fraction(-4, 2)  # Équivaut à -2
            self.assertTrue(frac.is_integer)

            # Fraction négative non entière
            frac = Fraction(-5, 2)  # Équivaut à -2.5
            self.assertFalse(frac.is_integer)

    def test_is_proper(self):
        # Cas simple : fraction propre
        frac = Fraction(3, 4)  # Numérateur < Dénominateur
        self.assertTrue(frac.is_proper)

        # Cas simple : fraction impropre
        frac = Fraction(5, 4)  # Numérateur > Dénominateur
        self.assertFalse(frac.is_proper)

        # Fraction réduite mais propre
        frac = Fraction(2, 6)  # Équivaut à 1/3
        self.assertTrue(frac.is_proper)

        # Fraction réduite mais impropre
        frac = Fraction(6, 3)  # Équivaut à 2
        self.assertFalse(frac.is_proper)

        # Fraction nulle (propre par définition)
        frac = Fraction(0, 5)  # Équivaut à 0/5
        self.assertTrue(frac.is_proper)

        # Fraction négative propre
        frac = Fraction(-3, 4)  # Numérateur < Dénominateur
        self.assertTrue(frac.is_proper)

        # Fraction négative impropre
        frac = Fraction(-5, 4)  # Numérateur > Dénominateur
        self.assertFalse(frac.is_proper)

    def test_is_adjacent_to(self):
        # Cas simple : fractions adjacentes
        frac1 = Fraction(1, 3)
        frac2 = Fraction(1, 2)
        self.assertTrue(frac1.is_adjacent_to(frac2))  # Différence = 1/6

        frac3 = Fraction(1, 4)
        self.assertTrue(frac1.is_adjacent_to(frac3))  # Différence = 1/12

        # Cas non adjacent : différence non unitaire
        frac4 = Fraction(2, 3)
        self.assertTrue(frac1.is_adjacent_to(frac4))  # Différence = 1/3

        # Cas avec une fraction négative (adjacent)
        frac5 = Fraction(-2, 3)
        frac6 = Fraction(-1, 3)
        self.assertTrue(frac5.is_adjacent_to(frac6))  # Différence = 1/3

        # Cas avec une fraction négative (non-adjacent)
        frac7 = Fraction(-3, 5)
        frac8 = Fraction(-1, 5)
        self.assertFalse(frac7.is_adjacent_to(frac8))  # Différence = 2/5

        # Cas avec des fractions impropres (adjacent)
        frac9 = Fraction(7, 3)
        frac10 = Fraction(8, 3)
        self.assertTrue(frac9.is_adjacent_to(frac10))  # Différence = 1/3

        # Cas avec des fractions impropres (non-adjacent)
        frac11 = Fraction(5, 2)
        frac12 = Fraction(7, 2)
        self.assertTrue(frac11.is_adjacent_to(frac12))  # Différence = 1

        #Cas avec Fraction est adjacente à elle-même
        frac13 = Fraction(-3, 9)
        self.assertFalse(frac13.is_adjacent_to(frac13))


        # Cas avec réduction automatique (adjacent)
        frac14 = Fraction(3, 6)  # Réduit à 1/2
        frac15 = Fraction(2, 6)  # Réduit à 1/3
        self.assertTrue(frac14.is_adjacent_to(frac15))  # Différence = 1/6


if __name__ == "__main__":
    unittest.main()
