import sys
import pygame
from pygame.locals import *
import random
import math

# Petit module qui permet de générer une grille de couleur aléatoire qu'on affiche.

def init(context):
    # On initialise pygame, la taille de la fenetre et la première itération de la grille
    # On retourne la surface qui sert à dessiner.
    pygame.init()
    surface = pygame.display.set_mode((context["frame_width"], context["frame_height"]))
    update(context)
    return surface

def mainLoop(context, surface):
    # Boucle principale, c'est ici qu'opère le coeur des opération.
    stop = False
    while not stop:
        # Même si pour le moment on ne gère que la cloture de la fenêtre, c'est ici qu'on récupère les entrées utilisateur.
        stop = processInput(context)

        # On met à jour la grille, c'est ici qu'on mettrais à jour le contexte du jeu.
        update(context)

        # On affiche le résultat.
        render(context, surface)
    pygame.quit()

def processInput(context):
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                # On peut mettre en pause la génération de grille avec espace.
                context["pause"] = not context["pause"]
    return False        

def update(context):
    # On génère une grille de la qui représente le nombre de "cellule" qu'on affiche, avec le contenu de chaque case qui contient un tuple qui représente la couleur RGB de la cellule.

    if context["pause"]: 
        return
    # on récupère l'arrondie supérieur pour pallier les cas où la taille de la fenêtre n'est pas multiple de l'échelle.
    grid_width = math.ceil(context["frame_width"] / context["frame_scale"])
    grid_height = math.ceil(context["frame_height"] / context["frame_scale"])
    context["grid"] = [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(grid_width)] for _ in range(grid_height)]

def render(context, surface):
    # On appels les différentes fonctions d'affichage, ensuite on applique la mise à jour.
    drawGrid(context, surface)
    pygame.display.update()

def drawGrid(context, surface):
    # Ici, pour chaque case de la grille, on génère un rectangle de cette couleur.
    grid = context["grid"]
    scale = context["frame_scale"]
    width = int(context["frame_width"] / context["frame_scale"])
    height = int(context["frame_height"] / context["frame_scale"])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (i * scale, j * scale, scale, scale))

def main():
    context = {
        "frame_width" : 400,
        "frame_height" : 400,
        "frame_scale" : 125,
        "pause" : False
    }

    surface = init(context)
    mainLoop(context, surface)

if __name__ == "__main__":
    main()