"""
Author: Nathanael Bayard
Module Name: Matrix
Description: functions to operate over lists of lists representing numerical matrices.
"""

from Bool import forall, not_, isNotZero
from List import zipWith, filterOutIx, firstIndex, grouped, mapLL, flatten
from Maybe import maybeMap

from Error import error

# some aliases used at the type level:
# /
#   Vector n = List n
#   Row n = List n
#   Column n = List n
#   Matrix n = List (Row n)
#   Family n = List (Vector n)
#   Dim = Int (expectedly, strictly superior to 0)
#   Index = Int (expectedly, superior or equal to 0)
# /
# most of the time, the type parameter `n` will
# be member of the type class `Num` which represents
# any type that can be seen and operated over as a number.
# beware that a class constraint like `[Num n]` applies to
# the whole of the type signature, not just the left side of
# the arrow.


#   checkDim : Int -> Void
def checkDim(dim):
    if dim <= 0:
        error(checkDim, "dimensions must be non null positive integers")

#   checkIx : Int . Int -> Void
def checkIx(index, limit):
    if index < 0 or index >= limit:
        error(checkIx, "index must be a natural integer inferior to "
               + "limit = " + str(limit))

# ==== constructors

#   nullVector : [Num n] Dim -> Vector n
def nullVector(dim):
    checkDim(dim)
    return [0 for i in range(dim)]

#   nullMatrix : [Num n] Dim . Dim -> Matrix n
def nullMatrix(n, p):
    checkDim(n)
    checkDim(p)
    return [nullVector(p) for j in range(n)]

# e.g.: unitVector(3,0) == [1, 0, 0]
#       unitVector(3,1) == [0, 1, 0]
#       unitVector(3,2) == [0, 0, 1]
# /
#   unitVector : [Num n] Int . Int -> Vector n
def unitVector(dim, i):
    checkDim(dim)
    checkIx(i, dim)
    z = nullVector(dim)
    z[i] = 1
    return z

# identity matrix of dimension dim
#   idMatrix : [Num n] Int -> Matrix n
def idMatrix(dim):
    checkDim(dim)
    return [unitVector(dim, i) for i in range(dim)]

# e.g.: matrixFromList([1,2,3,4,5,6], 2, 3) == [[1,2,3],
#                                               [4,5,6]]
#
#   matrixFromList : [Num n] List n . Int . Int -> Matrix n
def matrixFromList(xs, n, p):
    checkDim(n)
    checkDim(p)
    if len(xs) != n * p:
        error(matrixFromList, "wrong number of elements for input list")
    matrix = grouped(xs, p)
    return matrix

# ==== transformers

# listFromMatrix : [Num n] Matrix n -> List n
def listFromMatrix(matrix):
    return flatten(matrix)

# ==== queries

#   ncols : [Num n] Matrix n -> Int
def ncols(matrix):
    if len(matrix) == 0:
        error(ncols, "input matrix is an empty list")
    return len(matrix[0])

# the raising of an exception is not strictly
# necessary, yet a matrix of zero lines should
# not make any sense.
#
#   nrows : [Num n] Matrix n -> Int
def nrows(matrix):
    if len(matrix) == 0:
        error(nrows, "input matrix is an empty list")
    return len(matrix)

# can raise an exception if len(l) == 0.
#
#   isNullVector : [Num n] Vector n -> Bool
def isNullVector(l):
    return l == nullVector(len(l))

# can raise an exception if the matrix is not well formed.
#
#   isNullMatrix : [Num n] Matrix n -> Bool
def isNullMatrix(matrix):
    n = nrows(matrix)
    p = ncols(matrix)
    return matrix == nullMatrix(n, p)

# this function returns `Just` a list that maps, for each
# line of the input matrix, the index of the first non-zero
# element on that list.
# returns Nothing if one of the lines is full of zeroes.
# cf Maybe.py/maybeMap
# 
#   firstNonNullEachLine : [Num n] Matrix n -> Maybe (List Index)
def firstNonNullEachLine(matrix):
    return maybeMap(lambda line: firstIndex(isNotZero, line), matrix)
        # maybeMap : (a -> Maybe b) . List a -> Maybe (List b)
        # c.f. Maybe.py

# ==== modificators

#   columnAt : Index . Matrix t ->  Column t
def columnAt(index, matrix):
    p = ncols(matrix)
    checkIx(index, p)
    return map(lambda line: line[index], matrix)
      # maps each line to its nth element
    

#   transposed : Matrix t -> Matrix t
def transposed(matrix):
    n = nrows(matrix)
    p = ncols(matrix)
    return map(lambda index: columnAt(index, matrix), range(p))
      # maps each index of new line to the corresponding column
      # of the old matrix

#   negate : [Num n] Matrix n -> Matrix n
def negate(matrix):
    return mapMatrix(lambda x: -x, matrix)



#   mapMatrix : (a -> b) . Matrix a -> Matrix b
def mapMatrix(f, matrix):
    return mapLL(f, matrix)


# ==== families

# takes a matrix (list of lines) and returns
# the list of its columns.
# 
#   familyFromMatrix : Matrix t -> Family t
def familyFromMatrix(matrix):
    return transposed(matrix)

# takes a family (list of vectors) and returns
# the matrix whose columns are those vectors.
# 
#   matrixOfFamily : Family t -> Matrix t
def matrixOfFamily(family):
    return transposed(family)
