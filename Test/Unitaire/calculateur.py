import random
import heapq
def incremente(v):
    return v + 1

def decremente(v):
    return v - 1

def ajoute(v, n):
    for i in range(n):
        v = incremente(v)
    return v

def soustrait(v, n):
    for i in range(n):
        v = decremente(v)
    return v

def multiplie(v, n):
    resultat = 0
    for i in range(n):
        resultat = ajoute(resultat, v)
    return resultat

def divise(v, n):
    if n == 0:
        raise ZeroDivisionError
    resultat = 0
    while v >= n:
        v = soustrait(v, n)
        resultat += 1
    return resultat, v

def tri_par_tas(tableau):
    heapq.heapify(tableau)
    resultat = []
    while len(tableau) > 0:
        resultat.append(heapq.heappop(tableau))
    return resultat

def d6():
    return random.randint(1, 6)