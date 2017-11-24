# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: System
Description:
    type representing linear systems, and functions pertaining to them,
    like Gauss's method of resolution
"""

from List import zipWith, firstIndex, isolateItem, notFound, unzipWith, subtractLists, filterOutIx
from Bool import forall, isZero #, not_
from Maybe import Maybe, Just, Nothing
from Matrix import idMatrix, nullVector, firstNonNullEachLine, negate, unitVector, familyFromMatrix #, \
    # familyMatrixProd, completingBasis, isNullVector, isNullMatrix, matrixVecProd


class System():
    def __init__(self, pivotalLines, nonPivotalLines):
        self.pivotalLines = pivotalLines
        self.nonPivotalLines = nonPivotalLines
    def fromList(lines):
        pass
    def lastColIndex(self):
        if self.pivotalLines != []:
            return len(self.pivotalLines[0]) - 2
        elif self.nonPivotalLines != []:
            return len(self.nonPivotalLines[0]) - 2
        else:
            raise Exception() # should never happen

def isValidLine(line):
    leftSide = line[:-1]
    rightSide = line[-1]
    if forall(leftSide, isZero):
        return isZero(rightSide)
    else:
        return True

def maybeSystem(pivotalLines, nonPivotalLines):
    if forall(pivotalLines + nonPivotalLines, isValidLine):
        return Maybe(value = System(pivotalLines, nonPivotalLines))
    else: return Nothing

def maybeSystemFromMatrix(matrix, rightSide):
    def fuseToEnd(line, rightValue):
        return line + [rightValue]
    fusedLines = zipWith(fuseToEnd, matrix, rightSide)
    return maybeSystem([], fusedLines)
            
        
def findPivot(system, colIndex):
    def condition(line):
        return line[colIndex] != 0
    x= firstIndex(condition, system.nonPivotalLines)
    #print "findPivot", x, colIndex
    return x

def usePivot(system, pivotalLineIndex, colIndex):
    if notFound(pivotalLineIndex): # if the pivot was not found
        return Just(system) # do nothing
    (pivotalLine, nonPivotalLines) = \
        isolateItem(system.nonPivotalLines, pivotalLineIndex)
    pivot = pivotalLine[colIndex]
    #print "pivot", pivot
    def forEachLine(line):
        val = line[colIndex]
        coeff = val / pivot # fraction?
        #print "forEachLine", line, val, coeff
        return modifiedLine(line, pivotalLine, coeff)
    newPivotalLines = map(forEachLine, system.pivotalLines) + [pivotalLine]
    newNonPivotalLines = map(forEachLine, nonPivotalLines)
    return maybeSystem(newPivotalLines, newNonPivotalLines)

def modifiedLine(line, otherLine, coeff):
    def f(val, otherVal):
        return val - otherVal * coeff
    return zipWith(f, line, otherLine)

def echelonized(system, colIndex):
    #print "DBG"
    #printMatrix(system.pivotalLines)
    #print "ùùù"
    #printMatrix(system.nonPivotalLines)
    #print "¨¨¨"
    pivotalLineIndex = findPivot(system, colIndex)
    return usePivot(system, pivotalLineIndex, colIndex
        ).maybeDo(afterUsingPivot, colIndex)

def afterUsingPivot(system, colIndex):
    #print colIndex, system.lastColIndex()
    if colIndex >= system.lastColIndex(): # end of recursion?
        return Just(system)
    else:
        return echelonized(system, colIndex + 1)

def normalizedLine(line):
    firstNonZeroIndex = firstIndex(lambda val: val != 0, line)
    if notFound(firstNonZeroIndex):
        # the line is full of zeroes:
        #should never happen
        print "error: firstNonZeroIndex not found in normalizedLines"
        return line # do nothing
    firstNonZeroValue = line[firstNonZeroIndex]
    if firstNonZeroValue != 1:
        return map(lambda val: val / firstNonZeroValue, line)
    else: return line

def normalized(system):
    normalizedPivotalLines = map(normalizedLine, system.pivotalLines)
    #print "normalized"
    #printMatrix(normalizedPivotalLines)
    # check if some nonPivotalLines have non-empty values, esp in the last column (the right side of the equation)
    return maybeSystem(normalizedPivotalLines, system.nonPivotalLines)

def splitSides(line):
    leftSide = line[:-1]
    rightSide = line[-1]
    return (leftSide, rightSide)

def extractSolution(system):
    lines = system.pivotalLines
    if lines == []:
        dim = len(system.nonPivotalLines[0]) - 1
        return (idMatrix(dim), nullVector(dim))
    (leftMatrix, rightVector) = unzipWith(splitSides, lines)
    width = len(leftMatrix[0])
    pivotalColIndexes = firstNonNullEachLine(leftMatrix)
    nonPivotalColIndexes = subtractLists(range(width), pivotalColIndexes)
    leftMatrix = negate(leftMatrix)
    for index in nonPivotalColIndexes:
        uv = unitVector(width, index)
        leftMatrix.insert(index, uv)
        rightVector.insert(index, 0)
    #print "filled"
    #printMatrix(leftMatrix)
    kernelBasis = filterOutIx(pivotalColIndexes, familyFromMatrix(leftMatrix))
    particularSolution = rightVector
    return (kernelBasis, particularSolution)

def systemSolution(matrix, rightSide):
    maybeSolution = maybeSystemFromMatrix(matrix, rightSide
        ).maybeDo(echelonized, 0
        ).maybeDo(normalized
        ).maybeApply(extractSolution)
    return maybeSolution

#def testSolution(affine, matrix, rightSide):
#    (kerBasis, pSol) = affine
#    
#    #print "kb, m", kerBasis, matrix
#    dim = len(pSol)
#    kerBasisImage = familyMatrixProd(matrix, kerBasis)
#    kerBasisComplement = completingBasis(kerBasis, dim)
#    kerBasisComplementImage = familyMatrixProd(matrix, kerBasisComplement)
#    goodKerBasis = isNullMatrix(kerBasisImage) and \
#        forall(kerBasisComplementImage, not_(isNullVector))
#    goodPSol = matrixVecProd(matrix, pSol) == rightSide
#    #return goodKerBasis and matrixVecProd(matrix, pSol) == rightSide
#    
#    out = ""
#    if not goodKerBasis:
#        out += " badKerBasis "
#    if not goodPSol:
#        out += " badPSol " + str(matrixVecProd(matrix, pSol))
#    return out
