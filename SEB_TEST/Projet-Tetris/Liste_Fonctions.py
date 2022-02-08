
# SEF : du 12-01-2022 au 13-01-2022
# Import des modules
from turtle import bgcolor
import timerthread
import numpy as np
import Global as Global
import Fenetres as Fen
# fSEF : du 12-01-2022 au 13-01-2022

# SEF : du 12-01-2022 au 13-01-2022
# Fonction qui créé un nouveau tableau
# Param TailleX, TailleY, Type de données et Retourne le Tableau créé
def Create_Tableau(X, Y,Type):
    try:
        TAB_P = np.zeros((X,Y), Type)
        dim = TAB_P.shape
        if  Global.Mode_Debug == "O" : print ("Création TAB_P vide OK")
        if  Global.Mode_Debug == "O" : print ("nb de lignes de TAB_P = " + str(dim[0]))
        if  Global.Mode_Debug == "O" : print ("nb de colonnes de TAB_P = " + str(dim[1]))
        return TAB_P
    except :
        print('Erreur dans Create_Tableau : ')
# fSEF : du 12-01-2022 au 13-01-2022

# SEF : du 12-01-2022 au 13-01-2022
# Fonction qui écrit une valeur dans un tableau en X/Y
# Param Tableau, PosX, PosY, Valeur à Ecrire
def Ajout_Val_Tableau(TAB_P, X=10, Y=20, Valeur=str):
    try:
        if  Global.Mode_Debug == "O" : print ("Ajout Valeur " + str(Valeur) + " en : (" + str(X) + "," + str(Y) + ")")
        TAB_P[X][Y] = Valeur
    except :
        print('Erreur de Ajout_Val_Tableau : ')
# fSEF : du 12-01-2022 au 13-01-2022

# SEF : 26-01-2022
# Fonction Init
def Init_Tableau(TAB_P, X=10, Y=20, Valeur="X"):
    try:
        # Je remplis tout le tableau de vide "O"...
        for i in range(X):
            for j in range(Y):
                Ajout_Val_Tableau(TAB_P, i ,j, "O")
        # ... puis je remplis le contour (côté) "X"
        for i in range(Y):
            Ajout_Val_Tableau(TAB_P, 0 ,i, "X")
            Ajout_Val_Tableau(TAB_P, X-1 ,i, "X")
        # ... puis je remplis le contour (bas) "X"
        for i in range(X):
            Ajout_Val_Tableau(TAB_P, i ,0, "X")
        if  Global.Mode_Debug == "O" : print (TAB_P)
    except IndexError as e:
        print('Erreur Init_Tableau : ', e)
# fSEF : 26-01-2022


# SEF : 01-02-2022 au 07-02-2022
# Fonction Rafraichit_tableau
def MAJ_Tableau(TAB_P, Canvas_P, X_TAB_P, Y_TAB_P, Taille_P):
    try:
        print ("MAJ_Tableau")
        Canvas_P.delete('ALL')
        for i in range(Global.X_TAB):
            for j in range(Global.Y_TAB):
                #Code qui écrit la valeur
                #txt = Canvas_P.create_text(X_TAB_P * Taille_P - (i+1)*Taille_P + Taille_P/2, 
                #                                                     Y_TAB_P * Taille_P - (j+1)*Taille_P + Taille_P/2, 
                #                                                     text=TAB_P[i][j], font="Arial 16 italic", fill="blue")

                #Récupération de la couleur dans la liste Globale
                Couleur=Global.tab_couleur[Global.tab_lettre_piece.index(TAB_P[i][j])]
                if  Global.Mode_Debug == "O" : print('Couleur : X(' + str(i) + ")-Y(" + str(j) + ") = " + str(Couleur))
                # remplissage des carrés avec la couleur
                txt = Canvas_P.create_rectangle(X_TAB_P * Taille_P - (i+1)*Taille_P, 
                                                Y_TAB_P * Taille_P - (j+1)*Taille_P,
                                                X_TAB_P * Taille_P - (i+0)*Taille_P, 
                                                Y_TAB_P * Taille_P - (j+0)*Taille_P,
                                                fill=Couleur)

    except IndexError as e:
        print('Erreur MAJ_Tableau : ', e)
# fSEF : 01-02-2022 au 07-02-2022

# SEF : 08-02-2022
# Fonction qui lance le Game
def Start_Game(Fen_canvas):
    try:
        Global.Jeux_En_Cours = "O"
        if  Global.Mode_Debug == "O" : print (Global.Jeux_En_Cours)

        ## Lancement du Jeu ##
        run = True
        Thread_Algo = Timer(Global.Vitesse_Base, Algo_Game)
        if Nouvelle_Piece(Fen_canvas) :
            if Global.Jeux_En_Cours == "O" : Thread_Algo.start()
        else :
            Global.Jeux_En_Cours = "E"
    except IndexError as e:
        print('Start_Game : ', e)


# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui lance le Game
def Algo_Game(Fen_canvas):
    try:
        if Est_ce_qu_on_peut_descendre() : 
            Descendre_B(Fen_canvas)
            MAJ_Score()
            Nouvelle_Piece(Fen_canvas)
        else :
            Figer_Piece(Fen_canvas)
            Supprime_Ligne(Fen_canvas)
            Descendre_Tableau(Fen_canvas)
            MAJ_Score()
    except IndexError as e:
        print('Start_Game : ', e)


# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Pause_Game():
    Global.Jeux_En_Cours = "P"
    if  Global.Mode_Debug == "O" : print (Global.Jeux_En_Cours)
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Stop le Game
def Stop_Game():
    Global.Jeux_En_Cours = "N"
    if  Global.Mode_Debug == "O" : print (Global.Jeux_En_Cours)
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui lance le Game
def Deplacer_G(event):
    print ("Deplacer_G")
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Nouvelle_Piece(Fen_canvas):
    print ("Nouvelle_Piece")
    MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Est_ce_qu_on_peut_descendre():
    print ("Est_ce_qu_on_peut_descendre")
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Descendre_B(Fen_canvas):
    print ("Descendre_B")
    MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def MAJ_Score():
    print ("MAJ_Score")
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Figer_Piece(Fen_canvas):
    print ("Figer_Piece")
    MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Supprime_Ligne(Fen_canvas):
    print ("Supprime_Ligne")
    MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Descendre_Tableau(Fen_canvas):
    print ("Descendre_Tableau")
    MAJ_Tableau(Global.Tableau_Principal, Fen.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True
# fSEF : 08-02-2022

# SEF : 25-01-2022
# Fonction exemple simple pour test unitaire
def incremente(v):
    return v + 1

def ajoute(v, n):
    for i in range(n):
        v = incremente(v)
    return v
# fSEF : 25-01-2022

# SEF : du 17-01-2022 au 31-01-2022
# Fonction Init_Algo
def Init_Algo():
    try:
        Global.Grille_Principale = np.zeros((Global.X_TAB,Global.Y_TAB), str)
        Global.Tableau_Principal = Create_Tableau(Global.X_TAB, Global.Y_TAB, str)
        if  Global.Mode_Debug == "O" : print (Global.Tableau_Principal)
        Init_Tableau (Global.Tableau_Principal, Global.X_TAB, Global.Y_TAB, "X")
        if  Global.Mode_Debug == "O" : print (Global.Tableau_Principal)
    except IndexError as e:
        print('Erreur Init_Algo  : ', e)
# fSEF : du 17-01-2022 au 31-01-2022

# SEF : 18-01-2022
# Fct Main principale
def Main():
    Global.Main ()
    if  Global.Mode_Debug == "O" : print ("Main Fonction")
    Init_Algo ()

if __name__ == "__main__" :
    Fen.Main()
# fSEF : 18-01-2022
