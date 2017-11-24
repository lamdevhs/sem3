# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: Matrix
Description: functions to handle lists of lists representing numerical matrices.
"""
from Bool import forall, not_, isNotZero
from List import count, zipWith, filterOutIx, firstIndex

#def columnSize(matrix):
#    return len(matrix[0])


# constructors

def nullVector(dim):
    return [0 for i in range(dim)]

def nullMatrix(n, p):
    return [nullVector(p) for j in range(n)]

def unitVector(dim, i):
    z = nullVector(dim)
    z[i] = 1
    return z

def idMatrix(dim):
    return [unitVector(dim, i) for i in range(dim)]

def matrixFromList(xs, n, p):
    if len(xs) != n * p:
        raise Exception()
    matrix = nullMatrix(n, p)
    for i in range(n*p):
        lineIx = int(i) / int(p)
        colIx = i - lineIx * p
        matrix[lineIx][colIx] = xs[i]
    return matrix

# transformers
def listFromMatrix(matrix):
    return reduce(lambda xs, ys: xs + ys, matrix, [])

# queries
def ncols(matrix):
    return len(matrix[0])

def nrows(matrix):
    return len(matrix)

def isNullVector(l):
    return l != [] and l == [0 for i in len(l)]

def isNullMatrix(matrix):
    return matrix != [] and forall(matrix, isNullVector)

def firstNonNullEachLine(matrix):
    return map(lambda line: firstIndex(isNotZero, line), matrix)


# modificators
def transposed(matrix):
    if matrix == []:
        return []
    #n = len(matrix)
    p = len(matrix[0])
    def f(newlineIx):
        return map(lambda oldline: oldline[newlineIx], matrix)
    return map(f, range(p))

def negate(matrix):
    return mapMatrix(lambda x: -x, matrix)


# mapping
def mapMatrix(f, matrix):
    def g(line):
        return map(f, line)
    return map(g, matrix)





# math stuff
def familyFromMatrix(matrix):
    return transposed(matrix)

def matrixOfFamily(family):
    return transposed(family)

def kernelBasis(matrix, dim):
#    if matrix == [] or matrix[0] == []:
#        return matrix
#    dim = len(matrix[0])
    (kerBasis, _) = solution(matrix, nullVector(dim)).value
    return kerBasis

def matrixRank(matrix, dim):
    kerBasis = kernelBasis(matrix, dim)
    return dim - len(kerBasis)
    #return count(not_(isNullVector), reducedMat)

def familyRank(family):
    return matrixRank(matrixOfFamily(family))

def isFreeFamily(family):
    return familyRank(family) == len(family)

def isIn(vector, family, isFree = False):
    if family == []:
        return False
    dimSpace = len(vector)
    dimSubspace = familyRank(family)
    if dimSpace == dimSubspace:
        return True
    else:
        return familyRank(family + [vector]) == dimSubspace



# matrix product
def scalarMul(matrix, coeff):
    return mapMatrix(lambda term: term * coeff, matrix)
    
def add(x, y):
    return x + y
def multiply(x, y):
    return x * y


def scalarProd(v, w):
    if len(v) != len(w) or len(v) == 0:
        print "can't multiply those", v, w
        raise Exception()
    return reduce(add, zipWith(multiply, v, w))

def matrixVecProd(M, V):
    n = nrows(M)
    p = ncols(M)
    p2 = nrows(V)
    #q = 1
    if n == 0 or p == 0:
        return []
    if p != p2:
        print "can't multiply those:", M, V
        raise Exception()
    out = nullVector(p)
    for i in range(n):
        out[i] = scalarProd(M[i], V)
    return out

def matrixProd(M, N):
    n = nrows(M)
    p = ncols(M)
    p2 = nrows(N)
    q = ncols(N)
    tN = transposed(N)
    if n == 0 or p == 0 or q == 0:
        return []
    if p != p2:
        print "can't multiply those:", M, N
        raise Exception()
    out = nullMatrix(n, q)
    for i in range(n):
        for j in range(q):
            out[i][j] = scalarProd(M[i], tN[j])
    return out

def familyMatrixProd(matrix, family):
    return map(lambda vec: matrixVecProd(matrix, vec), family)


# basis
def completingBasis(echelonizedBasis, dim):
    indexes = firstNonNullEachLine(echelonizedBasis)
    unitaryVectors = idMatrix(dim)
    return filterOutIx(indexes, unitaryVectors)

def completedBasis(echelonizedBasis, dim):
    if echelonizedBasis == []:
        print "can't complete basis, unknown dimension"
        raise Exception()
    indexes = firstNonNullEachLine(echelonizedBasis)
    dim = len(echelonizedBasis[0])
    unitaryVectors = idMatrix(dim)
    return echelonizedBasis + filterOutIx(indexes, unitaryVectors)


    

    
    
#def printMatrix(matrix):
#    n = len(matrix)
#    if n == 0:
#        print "[empty matrix]"
#        return
#    p = len(matrix[0])
#    for i in range(n):
#        for j in range(p):
#            print matrix[i][j], " ",
#        print ""


def _tests():
    L = [[1,2,0,1,0,1],
                    [1,0,1,2,1,6],
                    [2,5,-2,1./2,0,4],
                    [1,1,-1,1./3,0,0]
                       ]
    R = [0,0,0,0,0,0]
    printMatrix(L)
    print gaussMethod(L, R)
    L = [[1,2,0,1,0,1],
                        [1,2,0,1,0,1],
                        [2,5,-2,1./2,0,4],
                        [1,1,-1,1./3,0,0]
                       ]
    R = [0,0,0,0,0,0]
    printMatrix(L)
    print gaussMethod(L, R)