# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 19:57:03 2022

@author: Marion, Sébastien et Sébastien
"""

# SEF : du 12-01-2022 au 13-01-2022
# Import des modules
import Fenetres as Fen
import Global as Global
# fSEF : du 12-01-2022 au 13-01-2022

# SEF : 18-01-2022
# Fct Main principale
def Main():
    Global.Main ()
    if  Global.Mode_Debug == "O" : print ("Main principal")
    Fen.Main ()
    assert True, "Text si vrai"
    assert False, "Text si faux"

if __name__ == "__main__" :
    Main()
# SEF : 18-01-2022

