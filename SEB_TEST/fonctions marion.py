#MF du 21-02_2022 au 22-02-2022
# Fonction qui vérifie le contenu de toutes les lignes du tableau

def Verification_Ligne():
    global verif_Ligne, Ligne_a_enlever, a , k
    a= 0
    k = 19
    verif_Ligne = 0
    Ligne_a_enlever = 0
    while a < k : 
       x = 1
       for x in range (9):
           if ( Tab_P[19-a][x]!=0):
               verif_Ligne = verif_Ligne + 1
               x = x + 1
           else:
               verif_Ligne = 0
               break
            if (verif_Ligne == 10):
                Supprimer_Ligne()
            else
            a = a +1

#Focntion qui supprime les lignes et fait descendre le tableau avec vérif.

def Supprimer_Ligne():
    global k, a, verif_Ligne
    for u in range( 19 -a):
        Tab_P[19-a-u] = Tab_P[18-a-u]
    verif_Ligne = 0
    k = k -1
    fot x in range (9):
        del Tabl_P[0][0]
        Tab_P[0].append(0)
    print(Tab_P)
    
#Fin MF 21-02-2022
