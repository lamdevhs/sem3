︠21d558db-3caa-4db7-8763-4ad88c360440s︠
def vec(L):
    return vector(QQ, L)

print "Exercice 1:"
Q4=VectorSpace(QQ,4)
L1=[1,0,1,-1]
L2=[2,5,0,-1/2]
L3=[1,0,1,3/2]
L4=[1,0,1/2,-1]

print "Q1:"
A = matrix(QQ, [L1, L2, L3, L4])
print "A est inversible ssi rang de A = 4, qui est la dimension de l'espace contenant les vecteurs qui la composent."
print "rank(A) ="
show(A.rank())
print "donc A est inversible"


print "\nQ2:"
print "solution de l'équation AM = At :"
At = A.transpose()
M = A.solve_right(At)
show(M)
print "verification: AM == At:"
show(A*M == A.transpose())

print "Q3:"
print "NA = AM = At d'ou NAA^-1 = AMA^-1 = N ="
N = A * M * A.inverse()
show(N)
print "verification: NA == At:"
show(N*A == A.transpose())


︡23215e05-a82b-4ea1-9671-7ec49cf1a7d0︡{"stdout":"Exercice 1:\n"}︡{"stdout":"Q1:\n"}︡{"stdout":"A est inversible ssi rang de A = 4, qui est la dimension de l'espace contenant les vecteurs qui la composent.\n"}︡{"stdout":"rank(A) =\n"}︡{"html":"<div align='center'>$\\displaystyle 4$</div>"}︡{"stdout":"donc A est inversible\n"}︡{"stdout":"\nQ2:\n"}︡{"stdout":"solution de l'équation AM = At :\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrr}\n-3 &amp; -\\frac{19}{5} &amp; 2 &amp; -\\frac{16}{5} \\\\\n\\frac{6}{5} &amp; \\frac{61}{25} &amp; -\\frac{4}{5} &amp; \\frac{63}{50} \\\\\n4 &amp; 5 &amp; -1 &amp; 4 \\\\\n0 &amp; -\\frac{4}{5} &amp; 0 &amp; -\\frac{1}{5}\n\\end{array}\\right)$</div>"}︡{"stdout":"verification: AM == At:\n"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"stdout":"Q3:\n"}︡{"stdout":"NA = AM = At d'ou NAA^-1 = AMA^-1 = N =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrr}\n\\frac{31}{25} &amp; \\frac{2}{5} &amp; \\frac{14}{25} &amp; -\\frac{8}{5} \\\\\n\\frac{13}{5} &amp; 1 &amp; -\\frac{3}{5} &amp; -4 \\\\\n\\frac{2}{5} &amp; 0 &amp; \\frac{3}{5} &amp; 0 \\\\\n\\frac{227}{50} &amp; -\\frac{1}{10} &amp; -\\frac{37}{50} &amp; -\\frac{23}{5}\n\\end{array}\\right)$</div>"}︡{"stdout":"verification: NA == At:\n"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"done":true}︡
︠4cb31034-0e4a-4ec3-a610-64c41d19b5d4︠

︡d2ec27d9-757b-4d61-9e6a-c8b7dbf9b680︡
︠de224d7c-bcdf-4796-9555-85183e64772d︠
print "Exercice 2:"
Q3=VectorSpace(QQ,3)
u1=vector(QQ,[2,1,1])
u2=vector(QQ,[3,0,1])
u3=vector(QQ,[2,0,-1])
B2 = [u1,u2,u3]

fE1 = u1 + 2*u2
fE2 = u2 - u3
fE3 = 3*u2

A = matrix(QQ, [fE1, fE2, fE3]).transpose()

print "Q1:"
print "la matrice A, representative de F dans la base B1, a pour vecteurs colonne les images"
print "des vecteurs e1,e2,e3 par f, dans la base B1, soit:"
show(A)

print "Q2:"
print "u1 ="
show(u1)
print "f(u1) = 2*f(e1)+f(e2)+f(e3) = A*u1 ="
fu1 = 2*fE1 + fE2 + fE3
show(fu1)
print "egalement, f(u1) = A*u1 ="
fu1_ = A*u1
show(fu1_)

print "f(u1) dans la base B2:"
Q3B2 = Q3.subspace_with_basis(B2)
fu1_B2 = vector(QQ, Q3B2.coordinates(fu1))
show(fu1_B2)

print "Q3:"
print "si P est la matrice dont les vecteurs colonnes sont les vecteurs de la famille B2,"
print "composee des vecteurs u1, u2 et u3 (bien que ce n'etait pas explicitement dit dans l'enonce)"
print "alors P est la matrice de passage de B1 vers B2. P ="
P = matrix(QQ, B2).transpose()
show(P)

print "Q4:"
print "on a alors [f(u1)]B2 = P^-1 * [f(u1)]BC ="
Pinv = P.inverse()
fu1_B2_2 = Pinv * fu1
show(fu1_B2_2)
print "on a bien l'égalité entre les coordonnées trouvées pour f(u1) dans B2 par les deux methodes:"
show(fu1_B2 == fu1_B2_2)
print ""

︡eb280da3-db65-4864-bffa-331631717a55︡{"stdout":"Exercice 2:\n"}︡{"stdout":"Q1:\n"}︡{"stdout":"la matrice A, representative de F dans la base B1, a pour vecteurs colonne les images\n"}︡{"stdout":"des vecteurs e1,e2,e3 par f, dans la base B1, soit:\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrr}\n8 &amp; 1 &amp; 9 \\\\\n1 &amp; 0 &amp; 0 \\\\\n3 &amp; 2 &amp; 3\n\\end{array}\\right)$</div>"}︡{"stdout":"Q2:\n"}︡{"stdout":"u1 =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(2,\\,1,\\,1\\right)$</div>"}︡{"stdout":"f(u1) = 2*f(e1)+f(e2)+f(e3) = A*u1 =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(26,\\,2,\\,11\\right)$</div>"}︡{"stdout":"egalement, f(u1) = A*u1 =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(26,\\,2,\\,11\\right)$</div>"}︡{"stdout":"f(u1) dans la base B2:\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(2,\\,8,\\,-1\\right)$</div>"}︡{"stdout":"Q3:\n"}︡{"stdout":"si P est la matrice dont les vecteurs colonnes sont les vecteurs de la famille B2,\n"}︡{"stdout":"composee des vecteurs u1, u2 et u3 (bien que ce n'etait pas explicitement dit dans l'enonce)\n"}︡{"stdout":"alors P est la matrice de passage de B1 vers B2. P =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrr}\n2 &amp; 3 &amp; 2 \\\\\n1 &amp; 0 &amp; 0 \\\\\n1 &amp; 1 &amp; -1\n\\end{array}\\right)$</div>"}︡{"stdout":"Q4:\n"}︡{"stdout":"on a alors [f(u1)]B2 = P^-1 * [f(u1)]BC =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(2,\\,8,\\,-1\\right)$</div>"}︡{"stdout":"on a bien l'égalité entre les coordonnées trouvées pour f(u1) dans B2 par les deux methodes:\n"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"stdout":"\n"}︡{"done":true}︡
︠5d423e50-2d94-45c3-a487-3029324f98dfs︠

print "Exercice 3:"
E=VectorSpace(QQ,5)
A=matrix(QQ,[[1,1,2,0,5],[1/2,-2,1/3,0,1],[0,0,0,1,2]])
show(A)
print "Q1:"
print "A étant la matrice dont S est le noyau, et A pouvant être consideree comme"
print "representant une application lineaire,"
print "on a déjà une justification, puisque tout noyau d'une applin est un sous espace"
print "de l'espace de depart, ici R5."
print "on peut aussi le prouver par linearite du produit matriciel:"
print "pour tout couple de solutions (v,w) dans S^2, et tout reel b, on a:"
print "A(bv + w) = bAb + Aw = b*0 + 0 = 0"
print "donc bv + w appartient a S."
print "donc toute combinaison linéaire de vecteurs de S est encore dans S, donc par def,"
print "S est un sous espace vectoriel de R5, qui est l'espace de départ de l'applin canoniquement"
print "associee a A."

print "on peut le verifier partiellement avec les vecteurs de la base de S:"
S = A.right_kernel()
BS = S.basis()
print "l'image de leur somme vaut bien:"
show(A*sum(BS))
print "donc leur somme est dans S."

print "Q2:"
print "dimension de S:"
show(S.dimension())
print "ou encore, cardinal d'une base de S:"
show(len(S.basis()))
print "ou encore, dim(R5) - rank(A) = 5 - rank(A) ="
show(E.dimension() - A.rank())


print "Q3:"
v1 = vector(QQ, [2,1,-24,-18,9])
v2 = vector(QQ, [0,-1/2,33/2,13,-13/2])
L = [v1,v2]
LM = matrix(QQ, L).transpose()
print "rang de la famille L:"
show(LM.rank())
print "le rang vaut la cardinalite de la famille, donc elle est libre."

print "Q4:"
print "vect(L) et S sont de meme dimension. donc ils sont egaux ssi"
print "une base de vect(L) est incluse dans S. S contient L est:"
show(v1 in S and v2 in S)
print "donc vect(L) == S, et par conséquence L est bien une base de S, puisque c'est une"
print "famille libre et generatrice."



︡4b559ba6-93f8-4712-95f3-3a2046c57c27︡{"stdout":"Exercice 3:\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrrr}\n1 &amp; 1 &amp; 2 &amp; 0 &amp; 5 \\\\\n\\frac{1}{2} &amp; -2 &amp; \\frac{1}{3} &amp; 0 &amp; 1 \\\\\n0 &amp; 0 &amp; 0 &amp; 1 &amp; 2\n\\end{array}\\right)$</div>"}︡{"stdout":"Q1:\n"}︡{"stdout":"A étant la matrice dont S est le noyau, et A pouvant être consideree comme\n"}︡{"stdout":"representant une application lineaire,\n"}︡{"stdout":"on a déjà une justification, puisque tout noyau d'une applin est un sous espace\n"}︡{"stdout":"de l'espace de depart, ici R5.\n"}︡{"stdout":"on peut aussi le prouver par linearite du produit matriciel:\n"}︡{"stdout":"pour tout couple de solutions (v,w) dans S^2, et tout reel b, on a:\n"}︡{"stdout":"A(bv + w) = bAb + Aw = b*0 + 0 = 0\n"}︡{"stdout":"donc bv + w appartient a S.\n"}︡{"stdout":"donc toute combinaison linéaire de vecteurs de S est encore dans S, donc par def,\n"}︡{"stdout":"S est un sous espace vectoriel de R5, qui est l'espace de départ de l'applin canoniquement\n"}︡{"stdout":"associee a A.\n"}︡{"stdout":"on peut le verifier partiellement avec les vecteurs de la base de S:\n"}︡{"stdout":"l'image de leur somme vaut bien:\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(0,\\,0,\\,0\\right)$</div>"}︡{"stdout":"donc leur somme est dans S.\n"}︡{"stdout":"Q2:\n"}︡{"stdout":"dimension de S:\n"}︡{"html":"<div align='center'>$\\displaystyle 2$</div>"}︡{"stdout":"ou encore, cardinal d'une base de S:\n"}︡{"html":"<div align='center'>$\\displaystyle 2$</div>"}︡{"stdout":"ou encore, dim(R5) - rank(A) = 5 - rank(A) =\n"}︡{"html":"<div align='center'>$\\displaystyle 2$</div>"}︡{"stdout":"Q3:\n"}︡{"stdout":"rang de la famille L:\n"}︡{"html":"<div align='center'>$\\displaystyle 2$</div>"}︡{"stdout":"le rang vaut la cardinalite de la famille, donc elle est libre.\n"}︡{"stdout":"Q4:\n"}︡{"stdout":"vect(L) et S sont de meme dimension. donc ils sont egaux ssi\n"}︡{"stdout":"une base de vect(L) est incluse dans S. S contient L est:\n"}︡{"html":"<div align='center'>$\\displaystyle \\mathrm{True}$</div>"}︡{"stdout":"donc vect(L) == S, et par conséquence L est bien une base de S, puisque c'est une\n"}︡{"stdout":"famille libre et generatrice.\n"}︡{"done":true}︡
︠0a864ad5-593b-4cb3-a3c6-0f93be575635s︠
print "Exercice 4:"
Q4=VectorSpace(QQ,4)
L1=[-202,0,576,-36]
L2=[12,-154,-144,9]
L3=[-93/2,0,173,-6]
L4=[-372,0,768,29]
L = [L1,L2,L3,L4]
C = matrix(QQ, L)
show(C)

print "Q1:"
print "polynome caracteristique de C, sous forme factorisee:"
P = C.charpoly()
show(P.factor())
print "le polynome est scinde dans R, les valeurs propres de C en sont les deux racines"
print "reelles suivantes, couplees avec leur ordre de multiplicite:"
roots = P.roots()
show(roots)

print "Q2:"
ID = identity_matrix(QQ, 4)
print "pour toute valeur propre a, dim(Ea) = dim(ker(C - aId)) = dim(Q4) - rank(C-aId)"
E77 = (C - 77*ID).right_kernel()
E_154 = (C + 154*ID).right_kernel()
print "dimension de E77:"
show(E77.dimension())
print "dimension de E-154:"
show(E_154.dimension())



print "Q3:"
print "la dimension de chaque espace propre est egale a l'ordre de multiplicite de"
print "la valeur propre correspondante en tant que racine du polynome characteristique"
print "de C. ou dit autrement la somme des dimensions des espaces propres vaut dim(Q4)"
print "donc C est diagonalisable. Sa base de diagonalisation B2 sera l'union de bases"
print "quelconques de chaque espace propre. matrice M2 de la famille/base B2:"

B77 = E77.basis()
B_154 = E_154.basis()
B2 = B77 + B_154
M2 = matrix(QQ, B2).transpose()
show(M2)
print "verification: M2.inverse() * C * M2 ="
show(M2.inverse()*C*M2)
print "on obtient une matrice diagonale."

print "Q4:"
print "l'ordre des vecteurs dans une base n'a pas d'importance, on peut donc choisir"
print "un ordre parmi tous ceux qui alternent un vecteur de la base de E77 et un vecteur"
print "de la base de E-154. M3 matrice de la base B3 qui a une permutation pres vaut B2:"
B3 = [B77[0], B_154[0], B77[1], B_154[1]]
M3 = matrix(QQ, B3).transpose()
show(M3)
print "verification: M3.inverse() * C * M3 ="
show(M3.inverse()*C*M3)
print "cette matrice est bien la matrice E."

︡ce2caffc-11ca-43f8-96dd-88422f232667︡{"stdout":"Exercice 4:\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrr}\n-202 &amp; 0 &amp; 576 &amp; -36 \\\\\n12 &amp; -154 &amp; -144 &amp; 9 \\\\\n-\\frac{93}{2} &amp; 0 &amp; 173 &amp; -6 \\\\\n-372 &amp; 0 &amp; 768 &amp; 29\n\\end{array}\\right)$</div>"}︡{"stdout":"Q1:\n"}︡{"stdout":"polynome caracteristique de C, sous forme factorisee:\n"}︡{"html":"<div align='center'>$\\displaystyle (x - 77)^{2} \\cdot (x + 154)^{2}$</div>"}︡{"stdout":"le polynome est scinde dans R, les valeurs propres de C en sont les deux racines\n"}︡{"stdout":"reelles suivantes, couplees avec leur ordre de multiplicite:\n"}︡{"html":"<div align='center'>[($\\displaystyle 77$, $\\displaystyle 2$), ($\\displaystyle -154$, $\\displaystyle 2$)]</div>"}︡{"stdout":"Q2:\n"}︡{"stdout":"pour toute valeur propre a, dim(Ea) = dim(ker(C - aId)) = dim(Q4) - rank(C-aId)\n"}︡{"stdout":"dimension de E77:\n"}︡{"html":"<div align='center'>$\\displaystyle 2$</div>"}︡{"stdout":"dimension de E-154:\n"}︡{"html":"<div align='center'>$\\displaystyle 2$</div>"}︡{"stdout":"Q3:\n"}︡{"stdout":"la dimension de chaque espace propre est egale a l'ordre de multiplicite de\n"}︡{"stdout":"la valeur propre correspondante en tant que racine du polynome characteristique\n"}︡{"stdout":"de C. ou dit autrement la somme des dimensions des espaces propres vaut dim(Q4)\n"}︡{"stdout":"donc C est diagonalisable. Sa base de diagonalisation B2 sera l'union de bases\n"}︡{"stdout":"quelconques de chaque espace propre. matrice M2 de la famille/base B2:\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrr}\n1 &amp; 0 &amp; 1 &amp; 0 \\\\\n-\\frac{1}{4} &amp; 0 &amp; 0 &amp; 1 \\\\\n0 &amp; 1 &amp; \\frac{1}{6} &amp; 0 \\\\\n-\\frac{31}{4} &amp; 16 &amp; \\frac{4}{3} &amp; 0\n\\end{array}\\right)$</div>"}︡{"stdout":"verification: M2.inverse() * C * M2 =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrr}\n77 &amp; 0 &amp; 0 &amp; 0 \\\\\n0 &amp; 77 &amp; 0 &amp; 0 \\\\\n0 &amp; 0 &amp; -154 &amp; 0 \\\\\n0 &amp; 0 &amp; 0 &amp; -154\n\\end{array}\\right)$</div>"}︡{"stdout":"on obtient une matrice diagonale.\n"}︡{"stdout":"Q4:\n"}︡{"stdout":"l'ordre des vecteurs dans une base n'a pas d'importance, on peut donc choisir\n"}︡{"stdout":"un ordre parmi tous ceux qui alternent un vecteur de la base de E77 et un vecteur\n"}︡{"stdout":"de la base de E-154. M3 matrice de la base B3 qui a une permutation pres vaut B2:\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrr}\n1 &amp; 1 &amp; 0 &amp; 0 \\\\\n-\\frac{1}{4} &amp; 0 &amp; 0 &amp; 1 \\\\\n0 &amp; \\frac{1}{6} &amp; 1 &amp; 0 \\\\\n-\\frac{31}{4} &amp; \\frac{4}{3} &amp; 16 &amp; 0\n\\end{array}\\right)$</div>"}︡{"stdout":"verification: M3.inverse() * C * M3 =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrrr}\n77 &amp; 0 &amp; 0 &amp; 0 \\\\\n0 &amp; -154 &amp; 0 &amp; 0 \\\\\n0 &amp; 0 &amp; 77 &amp; 0 \\\\\n0 &amp; 0 &amp; 0 &amp; -154\n\\end{array}\\right)$</div>"}︡{"stdout":"cette matrice est bien la matrice E.\n"}︡{"done":true}︡
︠2e71a6de-2147-4912-a27d-c26d38814776s︠
print "Exercice 5:"

def left(tupl):
    (x, _) = tupl
    return x

def spectre(M):
    P = M.charpoly()
    roots = map(left, P.roots())
    return roots

def A(n):
    L = []
    for i in range(n):
        for j in range(n):
            L.append((i + j) % 3)
    return matrix(QQ, n, L)

def quest3a():
    print "\nquestion 3a)"
    print "cherchons la plus petite valeur de n tel que"
    print "le spectre reel de A(n) ne soit pas vide et"
    print "ne soit pas egal a {0}:"
    n = 1
    while True:
        sp = spectre(A(n))
        if len(sp) != 0 and sp != [0]:
            break
        n += 1
    print "on trouve n ="
    show(n)
    print "A(n) ="
    show(A(n))
    print "polynome characteristique de A(n), sous forme factorisee dans R:"
    P = A(n).charpoly()
    show(P.factor())
    print "spectre reel de A(n):"
    show(sp)
    

    
quest3a()

def quest3b():
    print "\nquestion 3b)"
    R = range(1,50)
    out = []
    for n in R:
        sp = spectre(A(n))
        if n in sp:
            out.append(n)
            
    print "liste des n dans [1,49] pour"
    print "lesquelles Sp(A(n)) contient n:"
    show(out)
quest3b()
︡476ddca8-0425-4829-84bb-8af14ff3a349︡{"stdout":"Exercice 5:\n"}︡{"stdout":"\nquestion 3a)\ncherchons la plus petite valeur de n tel que\nle spectre reel de A(n) ne soit pas vide et\nne soit pas egal a {0}:\non trouve n =\n"}︡{"html":"<div align='center'>$\\displaystyle 3$</div>"}︡{"stdout":"A(n) =\n"}︡{"html":"<div align='center'>$\\displaystyle \\left(\\begin{array}{rrr}\n0 &amp; 1 &amp; 2 \\\\\n1 &amp; 2 &amp; 0 \\\\\n2 &amp; 0 &amp; 1\n\\end{array}\\right)$</div>"}︡{"stdout":"polynome characteristique de A(n), sous forme factorisee dans R:\n"}︡{"html":"<div align='center'>$\\displaystyle (x - 3) \\cdot (x^{2} - 3)$</div>"}︡{"stdout":"spectre reel de A(n):\n"}︡{"html":"<div align='center'>[$\\displaystyle 3$]</div>"}︡{"stdout":"\nquestion 3b)\nliste des n dans [1,49] pour"}︡{"stdout":"\nlesquelles Sp(A(n)) contient n:\n"}︡{"html":"<div align='center'>[$\\displaystyle 3$, $\\displaystyle 6$, $\\displaystyle 9$, $\\displaystyle 12$, $\\displaystyle 15$, $\\displaystyle 18$, $\\displaystyle 21$, $\\displaystyle 24$, $\\displaystyle 27$, $\\displaystyle 30$, $\\displaystyle 33$, $\\displaystyle 36$, $\\displaystyle 39$, $\\displaystyle 42$, $\\displaystyle 45$, $\\displaystyle 48$]</div>"}︡{"done":true}︡
︠ec2ef108-b670-4ad4-b1aa-16646dc6ef8d︠





︠8b024ca5-1672-4a7f-9f2d-371b13815265︠









