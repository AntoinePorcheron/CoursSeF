
# SEF : du 12-01-2022 au 13-01-2022
# Import des modules
import unittest
import Liste_Fonctions
# fSEF : du 12-01-2022 au 13-01-2022

# SEF : 25-01-2022
class TestIncremente(unittest.TestCase):
    def test_incremente(self):
        i = 0
        self.assertEqual(Liste_Fonctions.incremente(i), 1)

class TestAjoute(unittest.TestCase):
    def test_ajoute(self):
        i = 0
        self.assertEqual(Liste_Fonctions.ajoute(i, 4), 4)
        # Renvoie Faux : self.assertEqual(Liste_Fonctions.ajoute(i, 4), 5)
# fSEF : 25-01-2022

# SEF : 25-01-2022
# Fct Main principale
if __name__ == "__main__":
    unittest.main()
# fSEF : 25-01-2022
