
# SEF : du 12-01-2022 au 13-01-2022
# Import des modules from ast import While
import tkinter
#import ctypes # An included library with Python install.   
import Liste_Fonctions as Lst_Fct
import Global as Global
# fSEF : du 12-01-2022 au 13-01-2022


# SEF : du 12-01-2022 au 01-02-2022
def Fen_Main_Tkinter():
    try:

        # Lancement de l'algo
        Lst_Fct.Init_Algo ()

        # Création de la fenêtre
        Fen_Princip = tkinter.Tk()
        Fen_Princip.geometry(str(Global.X_FEN) + "x" + str(Global.Y_FEN))
        Fen_Princip.title ("Tétris Games")

        # Fenetre 
        Label_entete = tkinter.Label(Fen_Princip, text="Hello World")
        Label_entete.place(x=Global.X_FEN/2,y=5)

        ##----- Création du canevas -----##
        Fen_canvas = tkinter.Canvas(Fen_Princip, 
                                    width=Global.X_TAB * Global.Taille_Case, 
                                    height=Global.Y_TAB * Global.Taille_Case, 
                                    background='black')
        Lst_Fct.MAJ_Tableau(Global.Tableau_Principal, 
                            Fen_canvas, Global.X_TAB, 
                            Global.Y_TAB, Global.Taille_Case)
        Fen_canvas.place(x=5,y=20)

        ## Ajout d'un bouton Fermer ##
        Bouton_Quit=tkinter.Button(Fen_Princip, text="Fermer", command=Fen_Princip.quit)
        Bouton_Quit.place(x=Global.X_FEN-50,y=Global.Y_FEN-30)

        ## Ajout d'un bouton START ##
        Bouton_Start=tkinter.Button(Fen_Princip, text="START", width= 10, command=lambda:[Lst_Fct.Start_Game(Fen_canvas), Fen_Princip.text.set("Mode_Jeux : " + Global.Jeux_En_Cours)])
        Bouton_Start.place(x=Global.X_TAB*Global.Taille_Case+50,y=40)

        ## Ajout d'un bouton STOP ##
        Bouton_Stop=tkinter.Button(Fen_Princip, text="STOP", width= 10, command=lambda:[Lst_Fct.Stop_Game(), Fen_Princip.text.set("Mode_Jeux : " + Global.Jeux_En_Cours)])
        Bouton_Stop.place(x=Global.X_TAB*Global.Taille_Case+50,y=70)

        ## Info Jeux_En_Cours ##
        Fen_Princip.text = tkinter.StringVar()
        Fen_Princip.text.set ("Mode_Jeux : " + str(Global.Jeux_En_Cours))
        Label_Mode = tkinter.Label(Fen_Princip, textvariable=Fen_Princip.text)
        Label_Mode.place(x=Global.X_TAB*Global.Taille_Case+50,y=100)

        ## Ajout de champ pour insérer une valeur dans la Grille avec un bouton Ajoute ##
        Label_Pos_X = tkinter.Label(Fen_Princip, text="Position X :")
        Label_Pos_X.place(x=Global.X_FEN/2,y=Global.Y_FEN-200)
        Txt_Pos_X = tkinter.Entry(Fen_Princip)
        Txt_Pos_X.place(x=Global.X_FEN/2+100,y=Global.Y_FEN-200)

        Label_Pos_Y = tkinter.Label(Fen_Princip, text="Position Y :")
        Label_Pos_Y.place(x=Global.X_FEN/2,y=Global.Y_FEN-180)
        Txt_Pos_Y = tkinter.Entry(Fen_Princip)
        Txt_Pos_Y.place(x=Global.X_FEN/2+100,y=Global.Y_FEN-180)

        Label_Texte = tkinter.Label(Fen_Princip, text="Position Texte :")
        Label_Texte.place(x=Global.X_FEN/2,y=Global.Y_FEN-160)
        Txt_Texte = tkinter.Entry(Fen_Princip)
        Txt_Texte.place(x=Global.X_FEN/2+100,y=Global.Y_FEN-160)

        Bouton_Ajoute=tkinter.Button(Fen_Princip, 
                                     text="Ajoute", 
                                     command=lambda:[Lst_Fct.Ajout_Val_Tableau(Global.Tableau_Principal,
                                                                               Global.X_TAB-int(Txt_Pos_X.get()),
                                                                               int(Txt_Pos_Y.get())-1,
                                                                               Txt_Texte.get()),
                                                    Lst_Fct.MAJ_Tableau(Global.Tableau_Principal,
                                                                        Fen_canvas,
                                                                        Global.X_TAB,
                                                                        Global.Y_TAB,
                                                                        Global.Taille_Case)])
        Bouton_Ajoute.place(x=Global.X_FEN/2+100,y=Global.Y_FEN-140)

        ## Parametrage des Touches ##
        Fen_Princip.bind("<Left>",Lst_Fct.Deplacer_G)

       ## Lancement de la fennetre ##
        Fen_Princip.mainloop()

    except ValueError as e:
        print('Erreur Fen_Main_Tkinter: ', e)

# fSEF : du 12-01-2022 au 01-02-2022

# SEF : 18-01-2022
# Fct Main principale
def Main():
    Global.Main ()
    if Global.Mode_Debug == "O" : print ("Main Fenetre")
    Fen_Main_Tkinter ()

if __name__ == "__main__" :
    Main()
# fSEF : 18-01-2022
