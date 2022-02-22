
# SEF : du 12-01-2022 au 13-01-2022
# Import des modules
import Fenetres as Fen
# fSEF : du 12-01-2022 au 13-01-2022

# SEF : 18-01-2022
def Main():
    # Variable globale qui seront en paramètre en phase 2
    global  Mode_Debug, X_TAB, Y_TAB, Tableau_Principal, Taille_Case, Grille_Principale, \
            tab_couleur, tab_lettre_piece, X_FEN, Y_FEN, Jeux_En_Cours, Vitesse_Base, Piece_Courante, \
            Fen_canvas
    # Taille du tableau
    X_TAB = 10
    Y_TAB = 20
    # Taille Fenetre
    X_FEN = 500
    Y_FEN = 500
    # Taille d'un carré en pixel
    Taille_Case = 20
    Vitesse_Base = 1

    # "O" Affiche ou pas les Print
    Mode_Debug = "N"

    # Variable Globale
    Tableau_Principal = []
    Grille_Principale = []
# SD : 18-02-2022
    Piece_Courante = ["O", [0, 0], [0, 0], [0, 0], [0, 0]]
# fSD : 18-02-2022
    tab_couleur = ["black","white","blue","red","green","magenta","cyan","yellow","navy"]
    tab_lettre_piece=["O","X","I","C","L","S","T","M","N"]
    Jeux_En_Cours = "V" # O=OUI / N=NON / P=PAUSE / F=FIN / E=Erreur

# Fct Main principale
if __name__ == "__main__" :
    Fen.Main()
# SEF : 18-01-2022