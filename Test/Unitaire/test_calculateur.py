import calculateur
import unittest
from unittest.mock import patch

"""
On définit un ensemble de tests unitaire pour le module calculateur.py
Pour chaque fonction on définit une classe, qui contient un ensemble de méthodes de test pour tester différents aspects de la fonction au besoin.
Les tests doivent rester simple et ne tester qu'une fonction à la fois.
Des tests bien écrits et bien faits ont pour fonction :
1. De s'assurer du bon fonctionnement de chaque fonction prise les unes indépendamment des autres.
2. De fournir une trace du fonctionnement attendu du code.
3. Dans une moindre mesure, de faciliter la réécriture des fonctions tout en garantissant leurs fonctionnements après (on vérifie une non-régression.)

Il est inutile de faire 150 tests similaires pour une fonction, il est bien plus important et efficace de tester chaque cas "limite" d'une fonction.
"""


class TestIncremente(unittest.TestCase):
    """
    Classe de test qui hérite de unittest.TestCase pour qu'elle soit reconnu pour les tests unitaires.
    """

    def test_incremente(self):
        """
        On ne fait qu'un test, car l'opération est simple et n'a pas de cas limite.
        """
        i = 0
        self.assertEqual(calculateur.incremente(i), 1)

class TestDecrement(unittest.TestCase):
    def test_soustrait(self):
        i = 1
        self.assertEqual(calculateur.decremente(i), 0)

class TestAjoute(unittest.TestCase):
    def test_ajoute(self):
        i = 0
        self.assertEqual(calculateur.ajoute(i, 4), 4)

class TestAjoute(unittest.TestCase):
    def test_ajoute(self):
        i = 0
        self.assertEqual(calculateur.ajoute(i, 5), 5)

class TestAjoute(unittest.TestCase):
    def test_ajoute(self):
        i = 0
        self.assertEqual(calculateur.ajoute(i, 5), 5)

class TestSoustrait(unittest.TestCase):
    def test_soustrait(self):
        i = 5
        self.assertEqual(calculateur.soustrait(i, 5), 0)

class TestMultiplie(unittest.TestCase):
    def test_multiplie(self):
        i = 2
        self.assertEqual(calculateur.multiplie(i, 5), 10)


class TestDivise(unittest.TestCase):
    """
    Classe de test pour les divisions. On arrive sur un cas plus intéressant car plusieurs
    choses à tester, plusieurs cas limite.
    """
    def test_divise_sans_reste(self):
        i = 10
        quotient, reste = calculateur.divise(i, 5)
        self.assertEqual(quotient, 2)
        self.assertEqual(reste, 0)

    def test_divise_avec_reste(self):
        i = 9
        quotient, reste = calculateur.divise(i, 5)
        self.assertEqual(quotient, 1)
        self.assertEqual(reste, 4)
    
    def test_divise_zero(self):
        """
        Ici on test qu'une division par 0 remonte bien l'erreur de type "ZeroDivisionError".
        """
        i = 5
        with self.assertRaises(ZeroDivisionError):
            calculateur.divise(i, 0)

class TestTriParTas(unittest.TestCase):
    def test_tri_tas(self):
        """
        Ici, on fait un test sur un tri par tas pour vérifier qu'on obtient bien un tableau trié.
        """
        tableau = [9,8,7,6,5,4,3,2,1]
        self.assertListEqual(calculateur.tri_par_tas(tableau), [1,2,3,4,5,6,7,8,9])


@patch("random.randint")
class TestD6(unittest.TestCase):
    """
    Ici, on utilise @patch pour prévenir qu'on va "patcher" les appels à random.randint.
    En effet, le but d'un test unitaire étant de tester une fonction de manière ponctuelle,
    1. Le test ne concerne pas le module random.randint, mais seulement l'appel à d6.
    2. L'aléatoire n'a pas sa place, un test doit être constant.

    la syntaxe "@patch(xxx) est-ce qu'on appelle un décorateur.
    """
    def test_lance_de(self, mock_random_value):
        """
        On effectue un lancé de dé.
        On force le résultat du dé à 3 et on vérifie qu'on obtient bien trois.
        """
        mock_random_value.return_value = 3
        self.assertEqual(calculateur.d6(), 3)

if __name__ == "__main__":
    unittest.main()