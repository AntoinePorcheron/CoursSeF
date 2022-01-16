



class Arbre():
    def __init__(self,nom=''):
        self.label = nom
        self.G = None
        self.D = None

    def PrintValues(self):
        print(self.label)
        if self.G:
            self.G.PrintValues()
        if self.D:
            self.D.PrintValues()

    def EcritValues(self, Res_Ret = ""):
        print(self.label)
        match self.label :
            case "J":   Res_Ret = "J(" + self.D.EcritValues() + ")"
            case "A":   Res_Ret = "(" + self.G.EcritValues() + ") A (" + self.D.EcritValues() + ")"
            case "V":   Res_Ret = "(" + self.G.EcritValues() + ") V (" + self.D.EcritValues() + ")"
            case _  :   Res_Ret = self.label
        return Res_Ret

T = Arbre('A')
T.G = Arbre('X1')
T.D = Arbre('J')
T.D.D = Arbre('V')
T.D.D.G = Arbre('X2')
T.D.D.D = Arbre('J')
T.D.D.D.D = Arbre('X3')

T.PrintValues()
Res=T.EcritValues()
print("Res = " + Res)

