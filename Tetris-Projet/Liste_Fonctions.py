
import numpy as np

# SEF : du 12-01-2022 au 13-01-2022
# Fonction qui créé un nouveau tableau
def Create_Tableau(X, Y,Type):
    try:
        TAB_P = np.zeros((X,Y), Type)
        dim = TAB_P.shape
        print ("Création TAB_P vide OK")
        print("nb de lignes de TAB_P = " + str(dim[0]))
        print("nb de colonnes de TAB_P = " + str(dim[1]))
        return TAB_P
    except OSError:
        print('Erreur de création du tableau: ')
# fSEF : du 12-01-2022 au 13-01-2022

# SEF : du 12-01-2022 au 13-01-2022
# Fonction qui écrit une valeur dans un tableau en X/Y
def Ajout_Val_Tableau(TAB_P, X=10, Y=20, Valeur=str):
    try:
        print ("Ajout Valeur " + str(Valeur) + " en : (" + str(X) + "," + str(Y) + ")")
        TAB_P[X,Y] = Valeur
    except OSError:
        print('Erreur de création du tableau: ')
# fSEF : du 12-01-2022 au 13-01-2022

# SEF : du 17-01-2022 au 31-01-2022
# Fonction Main_Algo
def Main_Algo():
    try:
        Tableau_Principal = Create_Tableau(20 ,10, str)
        Ajout_Val_Tableau(Tableau_Principal, 11 ,1, "X")
        print (Tableau_Principal)
    except OSError:
        print('Main_Algo: ')
# fSEF : du 17-01-2022 au 31-01-2022
