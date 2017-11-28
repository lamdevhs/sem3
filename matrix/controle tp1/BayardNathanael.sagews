︠b17c5184-4e57-4ce3-9d03-717a326aec7fs︠
def vec(L):
    return vector(QQ, L)

print "Exo1:"

Q3=VectorSpace(QQ,3)
L_u1=[1,2,3]
L_u2=[2,5,6]
L_u3=[7,15,21]

u1 = vec(L_u1)
u2 = vec(L_u2)
u3 = vec(L_u3)

L_v=[19,46,57]

print "Q1:"

F1 = Q3.subspace([u1,u2,u3])
U = [u1,u2]
MU = matrix(QQ, U).transpose()
MUrank = MU.rank()
show("rang de la famille (u1,u2):")
show(MUrank)
show("on a égalité entre cardinalité et rang, donc U est libre")
show("dimension de F1:")
show(F1.dimension())
show("u1 et u2 sont dans F1 et U est libre et a même rang que la dimension de F1, donc c'est une base de ce sev.")

print "Q2:"
F1_ = Q3.subspace_with_basis(U)
coordU3 = F1_.coordinates(u3)
show("u3 est dans F1 par construction;")

show("alpha et beta sont par definition, les coordonees de u3 dans la base U.")
show("coordonnees de u3 dans U: " + str(coordU3))
show ("on a alpha = " + str(coordU3[0]))
show("et beta = " + str(coordU3[1]))


print "Q3:"

v = vec(L_v)

show("le vecteur v est-il bien dans F1?")
show(v in F1)
coordV = F1_.coordinates(v)
show("les coordonnees de v sont: " + str(coordV[0]) + " et " + str(coordV[1]))


︡db50edfc-b8a8-4d4b-ad40-2e3a35ea6636︡{"stdout":"Exo1:\n"}︡{"stdout":"Q1:\n"}︡{"html":"<div align='center'>rang de la famille (u1,u2):</div>"}︡{"html":"<div align='center'>$\\displaystyle 2$</div>"}︡{"html":"<div align='center'>on a égalité entre cardinalité et rang, donc U est libre</div>"}︡{"html":"<div align='center'>dimension de F1:</div>"}︡{"html":"<div align='center'>$\\displaystyle 2$</div>"}︡{"html":"<div align='center'>u1 et u2 sont dans F1 et U est libre et a même rang que la dimension de F1, donc c'est une base de ce sev.</div>"}︡{"stdout":"Q2:\n"}︡{"html":"<div align='center'>u3 est dans F1 par construction;</div>"}︡{"html":"<div align='center'>alpha et beta sont par definition, les coordonees de u3 dans la base U.</div>"}︡{"html":"<div align='center'>coordonnees de u3 dans U: [5, 1]</div>"}︡{"html":"<div align='center'>on a alpha = 5</div>"}︡{"html":"<div align='center'>et beta = 1</div>"}︡{"stdout":"Q3:\n"}︡{"html":"<div align='center'>le vecteur v est-il bien dans F1?</div>"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"html":"<div align='center'>les coordonnees de v sont: 3 et 8</div>"}︡{"done":true}︡
︠75b2fa33-e2ce-41af-87d4-68a1c52b66fb︠
print "Exo2:"

print "Q1"

A = matrix(QQ, [[1,-1,1,2,-1], [1,2,1,0,0]])
B = matrix(QQ, [[1],[2]])
show("A=")
show(A)

show("B=")
show(B)


print "Q2"
Lv=[13/12,-2/3,9/4,2/3,13/3]
vv = vector(QQ, Lv)
show("valeur de A*v =")
Avv = A*vv
show(Avv)
show("valeur identique à B:")
show(matrix(QQ, Avv).transpose() == B)

print "Q3"

show("Base de sol(H): est la base du noyau droit de A:")
rightK = A.right_kernel()
BrightK = rightK.basis()
show(BrightK)

print "Q4"

psol = A.solve_right(B).transpose()[0]
show("Sol(S)= l'ensemble des vecteurs qui peuvent s'écrire comme une somme d'un vecteur du noyau droit de A, et du vecteur suivant,")
show("qui est solution particulière du système :")
show(psol)

print "Q5"
show("X est solution de S si et seulement si X - Sol(S) est dans le noyau droit de A, d'où pour X = v:")
show((vv - psol) in rightK)



︡34d5d752-b886-4ab4-9347-d5c9780f3767︡{"stdout":"Exo2:\n"}︡{"stdout":"Q1\n"}︡{"html":"<div align='center'>A=</div>"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n1 &amp; -1 &amp; 1 &amp; 2 &amp; -1 \\\\\n1 &amp; 2 &amp; 1 &amp; 0 &amp; 0\n\\end{array}\\right)$</div>"}︡{"html":"<div align='center'>B=</div>"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{r}\n1 \\\\\n2\n\\end{array}\\right)$</div>"}︡{"stdout":"Q2\n"}︡{"html":"<div align='center'>valeur de A*v =</div>"}︡{"html":"<div align='center'>$\\displaystyle \\left(1,\\,2\\right)$</div>"}︡{"html":"<div align='center'>valeur identique à B:</div>"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"stdout":"Q3\n"}︡{"html":"<div align='center'>Base de sol(H): est la base du noyau droit de A:</div>"}︡{"html":"<div align='center'>[$\\displaystyle \\left(1,\\,0,\\,-1,\\,0,\\,0\\right)$, $\\displaystyle \\left(0,\\,1,\\,-2,\\,0,\\,-3\\right)$, $\\displaystyle \\left(0,\\,0,\\,0,\\,1,\\,2\\right)$]</div>"}︡{"stdout":"Q4\n"}︡{"html":"<div align='center'>Sol(S)= l'ensemble des vecteurs qui peuvent s'écrire comme une somme d'un vecteur du noyau droit de A, et du vecteur suivant,</div>"}︡{"html":"<div align='center'>qui est solution particulière du système :</div>"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\frac{4}{3},\\,\\frac{1}{3},\\,0,\\,0,\\,0\\right)$</div>"}︡{"stdout":"Q5\n"}︡{"html":"<div align='center'>X est solution de S si et seulement si X - Sol(S) est dans le noyau droit de A:</div>"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"done":true}︡
︠a9ee2276-c597-41d6-90fd-43f20409b24cs︠
print "Exo3:"

Q5=VectorSpace(QQ,5)

L1=[1,2,1,0,5]
L2=[0,2,1,4,5]
L3=[-1,0,1,0,0]
L4=[1,2,3,0,5]
L5=[1,2,1,6,0]

u1=vector(QQ,L1)
u2=vector(QQ,L2)
u3=vector(QQ,L3)
u4=vector(QQ,L4)
u5=vector(QQ,L5)

B=[u1,u2,u3,u4,u5]



print "Q1"

MB = matrix(QQ, B).transpose()
show("Tous les vecteurs de B sont dans Q5 et son rang vaut:")
show(MB.rank())
show("Ces vecteurs sont donc libres puisqu'il y en a 5, et c'est aussi la dimension de Q^5:")
show(Q5.dimension())
show("B est donc une base de Q^5 car c'est une famille libre de cardinalité égale à  la dimension de Q5.")


print "Q2"

L_M1=[[1,-2,3, 4, 5],[1, 0, 2, 3, 2],[2,-5, -6, 7, 0],[2, 6, 4, 3, 1],[1, 0, 2, 3, -3]]

M1 = matrix(QQ, L_M1)
show("M(f)_bc5 = M1 ="); show(M1)

print "Q3"
Lv=[1,21,54,3,-58]
v = vec(Lv)
fv = M1*v
show("Les coordonnées de f(v) dans la base canonique bc5 sont les composantes du vecteur M1*v, qui sont:")
show(Q5.coordinates(fv)) # ou encore list(fv)

print "Q4"
show("pour i dans[1,5], les vecteurs f(ui) dans la base B, affichés dans cet ordre et comme vecteurs colonnes de la matrice suivante:")
Q5_B = Q5.subspace_with_basis(B)
C1 = M1 * u1
C2 = M1 * u2
C3 = M1 * u3
C4 = M1 * u4
C5 = M1 * u5
Cs = [C1, C2, C3, C4, C5]
BCs = []
for C in Cs:
    BCs.append(Q5_B.coordinates(C))
    
M2 = matrix(QQ, BCs).transpose()
show(M2)


print "Q5"


show("par définition on aura alors: M2 = M(f)_B = ")
M2 = matrix(QQ, BCs).transpose()
show(M2)


print "Q6"

def trace(M):
    dim = M.ncols()
    tr = 0
    for i in range(dim):
        tr += M[i][i]
    return tr

show("trace de M1 == trace de M2:")
show(trace(M1) == trace(M2))
show("trace de l'endomorphisme f:")
show(trace(M1))

print "Q7"
P = MB.inverse()

show("P="); show(P)

print "Q8"

show("on doit avoir M1 = P^-1.M2.P et M2 = P.M1.P^-1")

show("premiere égalite:")
PiM2P = MB * M2 * P
show(PiM2P == M1)

show("deuxieme égalite:")
PM1Pi = P * M1 * MB
show(PM1Pi == M2)

︡02b5b57f-a9b9-4ba9-96c4-a80ffd6dacae︡{"stdout":"Exo3:\n"}︡{"stdout":"Q1\n"}︡{"html":"<div align='center'>Tous les vecteurs de B sont dans Q5 et son rang vaut:</div>"}︡{"html":"<div align='center'>$\\displaystyle 5$</div>"}︡{"html":"<div align='center'>Ces vecteurs sont donc libres puisqu'il y en a 5, et c'est aussi la dimension de Q^5:</div>"}︡{"html":"<div align='center'>$\\displaystyle 5$</div>"}︡{"html":"<div align='center'>B est donc une base de Q^5 car c'est une famille libre de cardinalité égale à  la dimension de Q5.</div>"}︡{"stdout":"Q2\n"}︡{"html":"<div align='center'>M(f)_bc5 = M1 =</div>"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n1 &amp; -2 &amp; 3 &amp; 4 &amp; 5 \\\\\n1 &amp; 0 &amp; 2 &amp; 3 &amp; 2 \\\\\n2 &amp; -5 &amp; -6 &amp; 7 &amp; 0 \\\\\n2 &amp; 6 &amp; 4 &amp; 3 &amp; 1 \\\\\n1 &amp; 0 &amp; 2 &amp; 3 &amp; -3\n\\end{array}\\right)$</div>"}︡{"stdout":"Q3\n"}︡{"html":"<div align='center'>Les coordonnées de f(v) dans la base canonique bc5 sont les composantes du vecteur M1*v, qui sont:</div>"}︡{"html":"<div align='center'>[$\\displaystyle -157$, $\\displaystyle 2$, $\\displaystyle -406$, $\\displaystyle 295$, $\\displaystyle 292$]</div>"}︡{"stdout":"Q4\n"}︡{"html":"<div align='center'>pour i dans[1,5], les vecteurs f(ui) dans la base B, affichés dans cet ordre et comme vecteurs colonnes de la matrice suivante:</div>"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n10 &amp; \\frac{7}{8} &amp; \\frac{29}{8} &amp; \\frac{31}{2} &amp; -\\frac{85}{8} \\\\\n-\\frac{38}{5} &amp; -\\frac{201}{20} &amp; \\frac{1}{20} &amp; -\\frac{37}{5} &amp; -\\frac{9}{20} \\\\\n-\\frac{109}{10} &amp; -\\frac{359}{20} &amp; -\\frac{31}{20} &amp; -\\frac{151}{10} &amp; -\\frac{261}{20} \\\\\n-\\frac{24}{5} &amp; \\frac{359}{40} &amp; -\\frac{139}{40} &amp; -\\frac{97}{10} &amp; \\frac{611}{40} \\\\\n\\frac{89}{10} &amp; \\frac{61}{5} &amp; \\frac{3}{10} &amp; \\frac{101}{10} &amp; \\frac{63}{10}\n\\end{array}\\right)$</div>"}︡{"stdout":"Q5\n"}︡{"html":"<div align='center'>par définition on aura alors: M2 = M(f)_B = </div>"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n10 &amp; \\frac{7}{8} &amp; \\frac{29}{8} &amp; \\frac{31}{2} &amp; -\\frac{85}{8} \\\\\n-\\frac{38}{5} &amp; -\\frac{201}{20} &amp; \\frac{1}{20} &amp; -\\frac{37}{5} &amp; -\\frac{9}{20} \\\\\n-\\frac{109}{10} &amp; -\\frac{359}{20} &amp; -\\frac{31}{20} &amp; -\\frac{151}{10} &amp; -\\frac{261}{20} \\\\\n-\\frac{24}{5} &amp; \\frac{359}{40} &amp; -\\frac{139}{40} &amp; -\\frac{97}{10} &amp; \\frac{611}{40} \\\\\n\\frac{89}{10} &amp; \\frac{61}{5} &amp; \\frac{3}{10} &amp; \\frac{101}{10} &amp; \\frac{63}{10}\n\\end{array}\\right)$</div>"}︡{"stdout":"Q6\n"}︡{"html":"<div align='center'>trace de M1 == trace de M2:</div>"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"html":"<div align='center'>trace de l'endomorphisme f:</div>"}︡{"html":"<div align='center'>$\\displaystyle -5$</div>"}︡{"stdout":"Q7\n"}︡{"html":"<div align='center'>P=</div>"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n-\\frac{1}{2} &amp; \\frac{13}{8} &amp; -\\frac{1}{2} &amp; -\\frac{3}{8} &amp; -\\frac{1}{4} \\\\\n0 &amp; -\\frac{3}{4} &amp; 0 &amp; \\frac{1}{4} &amp; \\frac{3}{10} \\\\\n-1 &amp; \\frac{5}{4} &amp; 0 &amp; -\\frac{1}{4} &amp; -\\frac{3}{10} \\\\\n\\frac{1}{2} &amp; -\\frac{7}{8} &amp; \\frac{1}{2} &amp; \\frac{1}{8} &amp; \\frac{3}{20} \\\\\n0 &amp; \\frac{1}{2} &amp; 0 &amp; 0 &amp; -\\frac{1}{5}\n\\end{array}\\right)$</div>"}︡{"stdout":"Q8\n"}︡{"html":"<div align='center'>on doit avoir M1 = P^-1.M2.P et M2 = P.M1.P^-1</div>"}︡{"html":"<div align='center'>premiere égalite:</div>"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"html":"<div align='center'>deuxieme égalite:</div>"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"done":true}︡
︠0d66c0dd-a688-4aa8-bf87-914a11fba017︠














