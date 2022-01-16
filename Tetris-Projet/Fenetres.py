
import pygame # par la même occasion cela importe pygame.locals dans l'espace de nom de Pygame
import ctypes # An included library with Python install.   
import Liste_Fonctions as Lst_Fct


# SEF : du 12-01-2022 au 13-01-2022
# Fenetre_vide ... pour l'instant
def Fen_Main():

    # Création de la fenêtre
    pygame.init()
    ecran = pygame.display.set_mode((300, 200))
    continuer = True

    # Lancement de l'algo
    Lst_Fct.Main_Algo ()

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                res = ctypes.windll.user32.MessageBoxW(0, "Etes-vous sur ?", "Fermeture", 4)
                print ("res = " + str(res) + " values")
                if res == 6:
                    continuer = False
                else:
                    continuer = True
    pygame.quit()
# fSEF : du 12-01-2022 au 13-01-2022
