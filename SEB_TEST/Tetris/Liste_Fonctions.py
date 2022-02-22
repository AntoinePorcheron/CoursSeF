
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
        if TAB_P.shape[-1] == 0 : del TAB_P
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
        if Global.Mode_Debug == "O" : print ("MAJ_Tableau")
        
        Canvas_P.delete('all')
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
                Canvas_P.create_rectangle(X_TAB_P * Taille_P - (i+1)*Taille_P+0, 
                                                Y_TAB_P * Taille_P - (j+1)*Taille_P+0,
                                                X_TAB_P * Taille_P - (i+0)*Taille_P+0, 
                                                Y_TAB_P * Taille_P - (j+0)*Taille_P+0,
                                                fill=Couleur, outline="black")
                #print(str(txt))
                #Global.Grille_Principale[i,j] = str(txt)


    except IndexError as e:
        print('Erreur MAJ_Tableau : ', e)
# fSEF : 01-02-2022 au 07-02-2022


# SEF : 08-02-2022
# Fonction Algo
def Algo_Game(Fen_Princip):
    try:
        # Mode PAUSE ==> On ne fait rien
        if Global.Jeux_En_Cours == "P" : 
            MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)

        # Mode STOP ==> On Ré-initialise le tableau
        if Global.Jeux_En_Cours == "N" : 
            Init_Tableau (Global.Tableau_Principal, Global.X_TAB, Global.Y_TAB, "X")
            MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)

        # Mode START ==> Le jeux est en cours : On déroule l'Algo
        if Global.Jeux_En_Cours == "O" :
            #time.sleep(Global.Vitesse_Base)
            if Est_ce_qu_on_peut_descendre() :
                Descendre_B()
            else :
                Figer_Piece()
                Supprime_Ligne()
                Descendre_Tableau()
                MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
                MAJ_Score()
                #time.sleep(1)
                Nouvelle_Piece()
            MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
        
        if Global.Mode_Debug == "O" : print ("Algo_Game : " + Global.Jeux_En_Cours)
        Fen_Princip.after(Global.Vitesse_Base*1000, Algo_Game, Fen_Princip)
        
    except IndexError as e:
        print('Algo_Game : ', e)
# fSEF : 09-02-2022

# SEF : 08-02-2022
# Fonction qui lance le Game
def Start_Game():
    
    # On ne relance pas un jeu si y'en a un en cours
    if Global.Jeux_En_Cours == "O" : return

    # On relance seulement si on est en pause
    if Global.Jeux_En_Cours == "P" : 
        Global.Jeux_En_Cours = "O"
        return

    ## Lancement d'un nouveau Jeu ##
    if Nouvelle_Piece() :
        MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
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

# SD : 18-02-2022
# Fonction qui déplace les cases de la pièce courante d'une case vers la gauche
def Deplacer_G(event):
    if Est_ce_qu_on_peut_aller_gauche():
        Imprime_Piece("O")
        Global.Piece_Courante[1][0] += 1
        Imprime_Piece(Global.Piece_Courante[0])
    if Global.Mode_Debug == "O" : print ("Deplacer_G")
    MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True

# Fonction qui teste si un déplacement vers la gauche de la pièce courante est possible
def Est_ce_qu_on_peut_aller_gauche():
    Imprime_Piece("O")
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+1, Global.Piece_Courante[1][1]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[2][0]+1, Global.Piece_Courante[1][1]+Global.Piece_Courante[2][1]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[3][0]+1, Global.Piece_Courante[1][1]+Global.Piece_Courante[3][1]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[4][0]+1, Global.Piece_Courante[1][1]+Global.Piece_Courante[4][1]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    return True
    if Global.Mode_Debug == "O" : print ("Est_ce_qu_on_peut_aller_gauche")
    return True

# Fonction qui lance le Game
def Deplacer_D(event):
    if Est_ce_qu_on_peut_aller_droite():
        Imprime_Piece("O")
        Global.Piece_Courante[1][0] -= 1
        Imprime_Piece(Global.Piece_Courante[0])
    if Global.Mode_Debug == "O" : print ("Deplacer_D")
    MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True

# Fonction qui teste si un déplacement vers la droite de la pièce courante est possible
def Est_ce_qu_on_peut_aller_droite():
    Imprime_Piece("O")
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]-1, Global.Piece_Courante[1][1]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[2][0]-1, Global.Piece_Courante[1][1]+Global.Piece_Courante[2][1]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[3][0]-1, Global.Piece_Courante[1][1]+Global.Piece_Courante[3][1]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[4][0]-1, Global.Piece_Courante[1][1]+Global.Piece_Courante[4][1]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    return True
    if Global.Mode_Debug == "O" : print ("Est_ce_qu_on_peut_aller_droite")
    return True

# Fonction qui pivote la pièce courante d'un quart de tour dans le sens anti horaire
def Pivoter_G(event):
    if Est_ce_qu_on_peut_pivoter_gauche():
        Imprime_Piece("O")
        Global.Piece_Courante[2]=[Global.Piece_Courante[2][1], -1*Global.Piece_Courante[2][0]]
        Global.Piece_Courante[3]=[Global.Piece_Courante[3][1], -1*Global.Piece_Courante[3][0]]
        Global.Piece_Courante[4]=[Global.Piece_Courante[4][1], -1*Global.Piece_Courante[4][0]]
        Imprime_Piece(Global.Piece_Courante[0])
    MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    if Global.Mode_Debug == "O" : print ("Pivoter_D")
    return True

# Fonction qui teste si on peut pivoter la pièce courante d'un quart de tour dans le sens anti horaire
def Est_ce_qu_on_peut_pivoter_gauche():
    Imprime_Piece("O")
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[2][1], Global.Piece_Courante[1][1]+-1*Global.Piece_Courante[2][0]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[3][1], Global.Piece_Courante[1][1]+-1*Global.Piece_Courante[3][0]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[4][1], Global.Piece_Courante[1][1]+-1*Global.Piece_Courante[4][0]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Mode_Debug == "O" : print ("Est_ce_qu_on_peut_pivoter_droite")
    # inutile de ré imprimer les lettres si on va retourner True car comme on va pivoter dans ce cas on va forcément les effacer
    return True

# Fonction qui pivote la pièce courante d'un quart de tour dans le sens horaire
def Pivoter_D(event):
    if Est_ce_qu_on_peut_pivoter_droite():
        Imprime_Piece("O")
        Global.Piece_Courante[2]=[-1*Global.Piece_Courante[2][1], Global.Piece_Courante[2][0]]
        Global.Piece_Courante[3]=[-1*Global.Piece_Courante[3][1], Global.Piece_Courante[3][0]]
        Global.Piece_Courante[4]=[-1*Global.Piece_Courante[4][1], Global.Piece_Courante[4][0]]
        Imprime_Piece(Global.Piece_Courante[0])
    if Global.Mode_Debug == "O" : print ("Pivoter_D")
    MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True

# Fonction qui teste si on peut pivoter la pièce courante d'un quart de tour dans le sens horaire
def Est_ce_qu_on_peut_pivoter_droite():
    Imprime_Piece("O")
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+-1*Global.Piece_Courante[2][1], Global.Piece_Courante[1][1]+Global.Piece_Courante[2][0]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+-1*Global.Piece_Courante[3][1], Global.Piece_Courante[1][1]+Global.Piece_Courante[3][0]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+-1*Global.Piece_Courante[4][1], Global.Piece_Courante[1][1]+Global.Piece_Courante[4][0]] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Mode_Debug == "O" : print ("Est_ce_qu_on_peut_pivoter_droite")
    # inutile de ré imprimer les lettres si on va retourner True car comme on va pivoter dans ce cas on va forcément les effacer
    return True

# Fonction qui crée une nouvelle pièce courante
def Nouvelle_Piece():
    i=np.random.choice([1, 2, 3, 4, 5, 6, 7])
    if i == 1:
        Global.Piece_Courante = ["I", [5, 19], [1, 0], [-1, 0], [-2, 0]]
    elif i == 2:
        Global.Piece_Courante = ["C", [5, 18], [0, 1], [-1, 1], [-1, 0]]
    elif i == 3:
        Global.Piece_Courante = ["L", [5, 18], [0, 1], [0, -1], [-1, -1]]
    elif i == 4:
        Global.Piece_Courante = ["S", [4, 18], [0, 1], [0, -1], [1, -1]]
    elif i == 5:
        Global.Piece_Courante = ["T", [5, 19], [1, 0], [-1, 0], [0, -1]]
    elif i == 6:
        Global.Piece_Courante = ["M", [5, 19], [1, 0], [0, -1], [-1, -1]]
    elif i == 7:
        Global.Piece_Courante = ["N", [5, 19], [-1, 0], [1, -1], [0, -1]]
    Imprime_Piece(Global.Piece_Courante[0])
    if Global.Mode_Debug == "O" : print ("Nouvelle_Piece")
    return True

# Fonction qui imprime la lettre entrée en paramètre dans le tableau principal à l'emplacement des cases de la Piece_Courante
def Imprime_Piece(lettre):
    Ajout_Val_Tableau(Global.Tableau_Principal, Global.Piece_Courante[1][0], Global.Piece_Courante[1][1], lettre)
    Ajout_Val_Tableau(Global.Tableau_Principal, Global.Piece_Courante[1][0]+Global.Piece_Courante[2][0], Global.Piece_Courante[1][1]+Global.Piece_Courante[2][1], lettre)
    Ajout_Val_Tableau(Global.Tableau_Principal, Global.Piece_Courante[1][0]+Global.Piece_Courante[3][0], Global.Piece_Courante[1][1]+Global.Piece_Courante[3][1], lettre)
    Ajout_Val_Tableau(Global.Tableau_Principal, Global.Piece_Courante[1][0]+Global.Piece_Courante[4][0], Global.Piece_Courante[1][1]+Global.Piece_Courante[4][1], lettre)
    if Global.Mode_Debug == "O" : print ("Imprime_Piece")
    return True

# Fonction qui teste si la pièce courante peut descendre, toujours TRUE pour l'instant
def Est_ce_qu_on_peut_descendre():
    Imprime_Piece("O")
    if Global.Tableau_Principal[Global.Piece_Courante[1][0], Global.Piece_Courante[1][1]-1] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[2][0], Global.Piece_Courante[1][1]+Global.Piece_Courante[2][1]-1] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[3][0], Global.Piece_Courante[1][1]+Global.Piece_Courante[3][1]-1] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Tableau_Principal[Global.Piece_Courante[1][0]+Global.Piece_Courante[4][0], Global.Piece_Courante[1][1]+Global.Piece_Courante[4][1]-1] != "O":
        Imprime_Piece(Global.Piece_Courante[0])
        return False
    if Global.Mode_Debug == "O" : print ("Est_ce_qu_on_peut_descendre")
    #myDatetime = datetime.now()
    #if Global.Mode_Debug == "O" : print (myDatetime)
    #if int(myDatetime.second) < 50 : return True
    Imprime_Piece(Global.Piece_Courante[0])
    return True


# Fonction qui modifie le tableau principal pour décaler les lettres de la variable Piece_Courante d'une case vers le bas
def Descendre_B():
    Imprime_Piece("O")
    Global.Piece_Courante[1][1] -= 1
    Imprime_Piece(Global.Piece_Courante[0])
    if Global.Mode_Debug == "O" : print ("Descendre_B")
    MAJ_Tableau(Global.Tableau_Principal, Global.Fen_canvas, Global.X_TAB, Global.Y_TAB, Global.Taille_Case)
    return True
# fSD : 18-02-2022


# SEF : 08-02-2022
# Fonction qui Pause le Game
def MAJ_Score():
    if Global.Mode_Debug == "O" : print ("MAJ_Score")
    return True
# fSEF : 08-02-2022

# SEF : 08-02-2022
# Fonction qui Pause le Game
def Figer_Piece():
    if Global.Mode_Debug == "O" : print ("Figer_Piece")
    return True
# fSEF : 08-02-2022

# MD
# Fonction Supprime les lignes
def Supprime_Ligne():
    if Global.Mode_Debug == "O" : print ("Supprime_Ligne")
    return True
# fMD

# MD
# Fonction Descend Tableau
def Descendre_Tableau():
    if Global.Mode_Debug == "O" : print ("Descendre_Tableau")
    return True
# fMD

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
