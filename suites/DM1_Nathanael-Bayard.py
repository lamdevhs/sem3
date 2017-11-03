import pylab as lab
import numpy as np
import matplotlib.patches as mpatches

        
# Nathanael Bayard, L2 Info, Suites et Series, DM, Nov 2017
# Les commentaires/conjectures se trouvent en fin de fichier.
# Agrandir la fenetre des graphiques au maximum pour un affichage optimal.



# -------- Outils - la version built-in est bizarre
def map(f, l): 
    out = []
    for i in range(len(l)):
        e = l[i]
        out.append(f(e))
    return out

# -------------------
# -------------------

def listeN(n):
    return range(n+1)
    
def left(e):
    (x,_) = e
    return x
def right(e):
    (_,x) = e
    return x

def separe(xs):
    leftList = map(left, xs)
    rightList = map(right, xs)
    return (leftList,rightList)

def feigenbaum(a, x):
    return 4 * a * x * (1 - x)

def f1(x):
    return feigenbaum(0.5, x)
def f2(x):
    return feigenbaum(0.7, x)
def f3(x):
    return feigenbaum(0.8, x)

def calculTerme(u0, f, n):
    out = u0
    for i in range(n):
        out = f(out)
    return out
    

# --------------------
# --------------------


def listeTerme(u0, f, n):    
    e = u0
    L = [e]
    while n != 0:
        e = f(e)
        L.append(e)
        n-=1
    return L

# methode de representation simple
def simple(subplot, u0, f, n):
    X = listeTerme(u0, f, n)
    Y = listeN(n)
    subplot.scatter(Y, X)

# ---------------------
# ---------------------

def motif(x, f):
    return [(x, x), (x, f(x))]

def lignePolygonale(f, u0, n):
    out = motif(u0, f)
    for i in range(n-1):
        (_, fx) = out[-1]
        out += motif(fx, f)
    return out

# methode de representation constructive
def constructive(subplot, u0, f, n):
    # j'affiche entre 0 et 1.2 pour laisser de la place
    # pour la legende a droite, cependant j'affiche y = f(x) uniquement entre
    # 0 et 1 pour eviter d'avoir une parabole qui part dans les negatifs
    # d'ou X et X2 au lieu de juste un seul X
    X = np.linspace(0,1.2,256, endpoint=True)
    X2 = np.linspace(0,1,256, endpoint=True)
    L = lignePolygonale(f, u0, n)
    V,W = separe(L)
    FX = f(X2)
    subplot.plot(X2, FX, 'g--') # g = green, parabole
    subplot.plot(X, X, 'b--') # b = blue, fonction identite
    subplot.plot(V, W, 'r-') # r = red, construction de la suite
    
    # affichage de la legende
    redLegend = mpatches.Patch(color='red', label='u(n+1) = f(u(n))')
    blueLegend = mpatches.Patch(color='blue', label='y = x')
    greenLegend = mpatches.Patch(color='green', label='y = f(x)')
    subplot.legend(handles=[redLegend, blueLegend, greenLegend])

# ----------------------
# ----------------------

def display(x, method, u0, N):
    (f, subplot, title) = x
    subplot.set_title(title)
    method(subplot, u0, f, N)

def loader():
    u0 = 0.01
    N = 30
    alphas = [0.5, 0.7, 0.8]
    functions = map(lambda alpha: lambda x: feigenbaum(alpha, x), alphas)
    titles = map(lambda alpha: "alpha = " + str(alpha), alphas)
    
    # rs = representation simple
    # rc = representation constructive
    
    # affichage de 2x3 graphiques separes
    # premiere ligne = representation simple
    # deuxieme ligne = representation constructive
    # chaque colonne dediee a une valeur de alpha differente
    # dans {0.5, 0.7, 0.8}
    _, ((rs1, rs2, rs3), (rc1, rc2, rc3)) = lab.subplots(2,3)
    
    # listes de triples: [(fonction, subplot, titre)]
    rsInput = zip(functions, [rs1, rs2, rs3], titles)
    rcInput = zip(functions, [rc1, rc2, rc3], titles)
    
    # pour chaque tuple dans rs/cInput, appeler 'display'
    # avec la methode d'affichage appropriee
    map(lambda x: display(x, simple, u0, N), rsInput)
    map(lambda x: display(x, constructive, u0, N), rcInput)
    lab.show()

loader()

# la fonction de Nicolas est maladroite
# car chaque appel a calculTerme(u0,f,i) dans la boucle
# calcule les premiers termes de 0 a i-1, meme s'ils ont
# deja ete precedemment calcules et enregistres dans
# la liste de sortie dans les boucles precedentes.


# Partie 1: representation graphique simple 
# on conjecture:
# . f1 croissante et convergeante vers une limite proche de ou egale a 0.5
# . f2 non monotone mais convergeante vers une limite entre 0.6 et 0.7
# . f3 non monotone et divergente de deuxieme espece

# Partie 2: representation constructive
# memes conjectures que dans la partie 1