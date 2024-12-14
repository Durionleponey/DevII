# Modifications apportées

## Constructeur
- Suppression de la précondition stricte sur num et den.
- Documentation claire des exceptions levées (FractionError si den=0 ou si num/den ne sont pas des entiers).
- Postcondition simplifiée : indique seulement que la fraction créée est valide et réduite.

## Méthodes __str__ et as_mixed_number
- Retrait des préconditions inutiles dans __str__.
- Postcondition d’as_mixed_number précisant désormais clairement le format de la chaîne renvoyée ("X", "X + Y/Z", "X - Y/Z", "0 + Y/Z", "0 - Y/Z").

## Méthodes arithmétiques (add, sub, mul, truediv, pow, eq)
- Plus de préconditions mentionnées, seulement une documentation des exceptions en cas de paramètre invalide.
- Pour __truediv__, ajout d’une précision sur la division par zéro (FractionError levée).

## is_zero
- Simplification du code : utilisation directe de `return self.numerator == 0`.

## Tests
- Ajout de nombreux cas de test couvrant les fractions positives, négatives, nulles, impropres, etc.
- Amélioration de la couverture des différentes méthodes.

## Couverture
- Analyse plus fine des lignes couvertes et non couvertes par les tests.
