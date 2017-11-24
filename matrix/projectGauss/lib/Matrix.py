# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: Matrix
Description: functions to handle lists of lists representing numerical matrices.
"""
from Bool import forall, not_, isNotZero
from List import zipWith, filterOutIx, firstIndex, grouped

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
    matrix = grouped(xs, p)
 #   matrix = nullMatrix(n, p)
 #   for i in range(n*p):
 #       lineIx = int(i) / int(p)
 #       colIx = i - lineIx * p
 #       matrix[lineIx][colIx] = xs[i]
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

# family stuff
def familyFromMatrix(matrix):
    return transposed(matrix)

def matrixOfFamily(family):
    return transposed(family)
