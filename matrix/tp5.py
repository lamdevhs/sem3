# -*- coding: utf-8 -*-
from __future__ import print_function
from fractions import *
from shutil import copy
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#.............................................................................
#E: M liste de listes (sans contrainte de type ni de taille)
#   M peut contenir: entier, float, string, Fraction
#affichage en colonnes de largeur constante = longueur maximale + 3
#S: --
def affiche_str (M):
    maxi=0
    for L in M:
        for val in L:
            if len(str(val))>maxi:
                maxi=len(str(val))
    chaine_format="%"+ str(maxi+3) + "s"
    for L in M:
        for val in L:
            print(chaine_format  %(val), end="")
        print("")
    print("")


#..........................................................................................
#E: m matrice
#   i1,i2 entiers        
#si possible, remplacer la ligne L(i1) par L(i1)+a2*L(i2) dans la matrice m
#sinon affichage d'erreur et arret de l'execution
#S: m modifié (procédure) 
def ajouter(m,i,a,j):
    if i<0 or i>=len(m) or j<0 or j>=len(m) :
        print("pb in comblin: parametre invalide.")
        exit()
    for k in range(0,len(m[0])):
        m[i][k]=m[i][k] + a*m[j][k]

     
#...........................................................................................


def map(f, xs):
    out = []
    for x in xs:
        out.append(f(x))
    return out

def ex1():
    v1 = Fraction(2,4) + 2 + 2*Fraction(1,4)
    print(v1)
    v2 = Fraction(1,2)**2
    print(v2)
    v3 = Fraction(1,2)*1.0
    print(v3)
    m = [
        [Fraction(10,20), -1, Fraction(2,3)],
        [Fraction(3,4)+Fraction(1,2), 2*Fraction(4,8),
           Fraction(1,2)*Fraction(5,6)]
    ]
    
    affiche_str(m)
    affiche_str(swap(m,0,1))
    affiche_str(expandLine(m, 1,100))
    sys = gaussMethod(m)
    print("gauss")
    affiche_str(sys)


def swap(m,i,j):
    if i < 0 or i >= len(m) or j < 0 or j >= len(m):
        print("normalizeLine: wrong input")
        exit()
    m[i], m[j] = m[j], m[i]
    return m
    
def expandVector(v, coeff):
    def f(e):
        return e*coeff
    return map(f, v)

def expandLine(m, i, coeff):
    if i < 0 or i >= len(m):
        print("normalizeLine: wrong value: i = " + str(i))
        exit()
    m[i] = expandVector(m[i], coeff)
    return m

def transvect(m, i, a, j):
    ajouter(m, a, i, j)
    return m

def transvectLine(v, a, v2):
    out = []
    for i in range(len(v)):
        out.append(v[i] + a * v2[i])
    return out
    
def findPivotLine(m, colIx):
    col = column(m, colIx)[colIx:]
    return findPivot(col) + colIx
    
def findPivot(v):
    p = -1
    for i in range(len(v)):
        if v[i] != 0:
            p = i
            break
    return p

def column(m, ix):
    if m == []:
        print("column: wrong input m")
        exit()
    if ix < 0 or ix >= len(m[0]):
        print("column: wrong input ix")
        exit()
    def f(line):
        return line[ix]
    return map(f, m)

def gaussMethod(sys):
    if len(sys) < 1:
        print ("gaussMethod: wrong input")
        exit()
    eqNb = len(sys)
    print(eqNb)
    varNb = len(sys[0]) - 1
    print(varNb)
    def recur(colIx, sys):
        pivotLineIx = findPivotLine(sys, colIx)
        print(pivotLineIx)
        if pivotLineIx >= 0: # the pivot exist, column not empty
            pivotLine = sys[pivotLineIx]
            print(pivotLine)
            pivotVal = pivotLine[colIx]
            print("pivotVal", pivotVal)
            swap(sys, pivotLineIx, colIx) # aka nth pivot to the nth line
            def f(line):
                coeff = line[colIx] / pivotVal
                return transvectLine(line, -coeff, pivotLine)
            sys = map(f, sys)
            sys[pivotLineIx] = pivotLine # replace the nullified line
        if colIx == varNb - 1: # we stop
            return sys
        else:
            return recur(colIx + 1, sys)
    recur(0, sys)
    return sys
    
       
ex1()
