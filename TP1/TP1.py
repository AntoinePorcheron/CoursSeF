




###### début de la construction de l'arbre binaire ###########
from binarytree import Node

class Arbre():
    def __init__(self,nom=''):
        self.label = nom
        self.G = None
        self.D = None
    def printValues(self):
        print(self.label)
        if self.G:
            self.G.printValues()
        if self.D:
            self.D.printValues()

T = Arbre('A')
T.G = Arbre('X1')
T.D = Arbre('J')
T.G.D = Arbre('V')
T.G.D.G = Arbre('X2')
T.G.D.D = Arbre('J')
T.G.D.G = Arbre('X3')
T.printValues()

######fin de la construction de l'arbre binaire###########




