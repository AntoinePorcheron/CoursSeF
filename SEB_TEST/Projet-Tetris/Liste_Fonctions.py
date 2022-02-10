
# SEF : du 12-01-2022 au 13-01-2022
# Import des modules
#from turtle import bgcolor
from datetime import datetime
from sqlite3 import Time
import time
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
        #Canvas_P.delete('ALL')
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
def Algo_Game(Fen_Princip, Fen_canvas):
    try:
        # Mode PAUSE ==> On ne fait rien
        if Global.Jeux_En_Cours == "P" : 
            MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)

        # Mode STOP ==> On Ré-initialise le tableau
        if Global.Jeux_En_Cours == "N" : 
            Init_Tableau (Global.Tableau_Principal, Global.X_TAB, Global.Y_TAB, "X")
            MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)

        # Mode START ==> Le jeux est en cours : On déroule l'Algo
        if Global.Jeux_En_Cours == "O" :
            #time.sleep(Global.Vitesse_Base)
            if Est_ce_qu_on_peut_descendre() :
                Descendre_B()
            else :
                Figer_Piece()
                Supprime_Ligne()
                Descendre_Tableau()
                MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
                MAJ_Score()
                time.sleep(1)
                Nouvelle_Piece()
            MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
        
        print ("Algo_Game : " + Global.Jeux_En_Cours)
        Fen_Princip.after(Global.Vitesse_Base*1000, Algo_Game, Fen_Princip, Fen_canvas)
        
    except IndexError as e:
        print('Algo_Game : ', e)
# fSEF : 09-02-2022

# SEF : 08-02-2022
# Fonction qui lance le Game
def Start_Game(Fen_canvas):
    
    # On ne relance pas un jeu si y'en a un en cours
    if Global.Jeux_En_Cours == "O" : return

    # On relance seulement si on est en pause
    if Global.Jeux_En_Cours == "P" : 
        Global.Jeux_En_Cours = "O"
        return

    ## Lancement d'un nouveau Jeu ##
    if Nouvelle_Piece() :
        MAJ_Tableau(Global.Tableau_Principal, Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
        Global.Jeux_En_Cours = "O"

    if  Global.Mode_Debug == "O" : print (Global.Jeux_En_Cours)

# Fonction qui Pause le Game
def Pause_Game():
    Global.Jeux_En_Cours = "P"
    if  Global.Mode_Debug == "O" : print (Global.Jeux_En_Cours)
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

# SEF : 10-02-2022
# Fonction qui lance le Game
def Deplacer_D(event):
    print ("Deplacer_D")
    return True
# fSEF : 10-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Nouvelle_Piece():
    print ("Nouvelle_Piece")
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Est_ce_qu_on_peut_descendre():
    print ("Est_ce_qu_on_peut_descendre")
    myDatetime = datetime.now()
    print (myDatetime)
    if int(myDatetime.second) < 50 : return True
    return False
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Descendre_B():
    print ("Descendre_B")
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
def Figer_Piece():
    print ("Figer_Piece")
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Supprime_Ligne():
    print ("Supprime_Ligne")
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Descendre_Tableau():
    print ("Descendre_Tableau")
    return True
# fSEF : 08-02-2022

# SEF : 25-01-2022
# Fonction exemple simple pour test unitaire
def incremente(v):
    return v + 1

def Affiche_Log():
    print("Affiche_Log")

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
