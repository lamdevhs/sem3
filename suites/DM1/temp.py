from pylab import *
import numpy as np

def listeN(n):
    return range(n+1)

def map(f, l):
    out = []
    for i in range(len(l)):
        e = f(l[i])
        out.append(e)
    return out
    
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

# la fonction de Nicolas est maladroite
# car chaque appel a calculTerme(u0,f,i)
# calcule les i+1 premiers termes, meme s'ils sont
# deja ete precedemment calcules et enregistres dans
# la liste de sortie.
def listeTerme(u0,f,n):    
    L = [u0]
    e = u0;
    while n != 0:
        e = f(e)
        L.append(e)
        n-=1
    return L

def scatterTerms(u0, f, n):
    X = listeTerme(u0, f, n)
    Y = listeN(n)
    scatter(Y, X)

u0 = 0.01
N = 15
#scatterTerms(u0, f1, N)
#scatterTerms(u0, f2, N)
#scatterTerms(u0, f3, N)
show()

# on conjecture f1 croissante et convergeante,
# f2 non monotone et convergeante,
# f3 non monotone et divergente (pas vers l'infini).

def motif(x, f):
    return [(x, x), (x, f(x))]

def lignePolygonale(f, u0, n):
    out = motif(u0, f)
    for i in range(n-1):
        latestTup = out[len(out) - 1]
        (_, fx) = latestTup
        out += motif(fx, f)
    return out

X = np.linspace(0,1,256, endpoint=True)
C, S = f1(X), X
L = lignePolygonale(f1, 0.01, 15)
V,W = separe(L)
plot(X, C)
plot(X, S)
plot(V, W)

def t():
    print listeN(5)
    xs = [(1,2),(3,4),(5,6)]
    print separe(xs)
    def f(x):
        return x + 1;
    print calculTerme(1,f,0)
    print calculTerme(1,f,2)
    print listeTerme(0,f,0)
    print listeTerme(0,f,5)
    
    print lignePolygonale(f,0,0)
    


t()