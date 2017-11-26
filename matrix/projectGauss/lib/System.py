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
from Matrix import idMatrix, nullVector, firstNonNullEachLine, negate, unitVector, familyFromMatrix


# ==== General Description of the algorithm:
#
# the function that is called first is
#    systemSolution : [Num n] Matrix n . Vector n -> Maybe (Solution n) [!]
# with
#    Solution n = (Maybe (Family n), Vector n)
#
# the first argument of `systemSolution` is the matrix `A` in
# the equation `AX = Y`, the second argument is the vector `Y`.
#
# the first element of the type `Solution n` represents the basis
# of the kernel of A, or Nothing if the kernel is reduced to
# the null vector.
# the second element of `Solution n` is of course the particular
# solution of the system found.
#
# if the system can't be solved, because at some point during
# the algorithm, we ended up with an equation of `0 = x`, with
# `x != 0`, then the result of `systemSolution` will be Nothing.


#   systemSolution : [Num n] Matrix n . Vector n -> Maybe (Solution n) [!]
def systemSolution(matrix, rightSide):
    maybeSystem = maybeSystemInit(matrix, rightSide
        ).maybeDo(echelonized, 0)
    if maybeSystem == Nothing:
        return Nothing
    else:
        system = maybeSystem.justValue()
        if len(system.pivotalLines) == 0:
        # extreme case: no pivot was found
        # during the echelonizing (which means the leftside
        # matrix A is null) and yet its result
        # is not Nothing, so the system does admit some
        # solution, so we conclude Y = 0 too,
        # and the kernel is thereafter the whole domain
        # of the linear application that could be
        # associated with A (if A has p columns,
        # that would canonically be R^p).
        # A particular solution can be any vector at all,
        # like the vector null.
            p = system.leftSideWidth
            return (Just(idMatrix(dim)), nullVector(dim))
        else:
            pivotalLines = keepPivotalLines(system)
        return Just(extractSolution(normalized(pivotalLines)))

# ==== next step:
# `systemSolution` calls 
#    maybeSystemInit : [Num n] Matrix n . Vector n -> Maybe (System n) [!]
#
# this function fuses/zips the elements of the rightside vector to the end
# of each line of the left matrix.

# then it calls the constructor `maybeSystem` with parameters
# `pivotalLines = []` and `nonPivotalLines` as the previous result of
# the gluing of both sides of the equation.

# example: if the equation of the system is
# 0 1 2 | x   9
# 3 4 5 | y = 9
# 6 7 8 | z   9
# then `maybeSystemInit would call:
#     maybeSystem([], [ [0,1,2,9], [3,4,5,9], [6,7,8,9] ])

#   maybeSystemInit : [Num n] Matrix n . Vector n -> Maybe (System n) [!]
def maybeSystemInit(matrix, rightSide):
    def fuseToEnd(line, rightValue):
        return line + [rightValue]
    fusedLines = zipWith(fuseToEnd, matrix, rightSide)
    return maybeSystem([], fusedLines)

# ==== next step:
# `maybeSystem` is a 'smart' constructor that returns Nothing if
# any line in either of its parameters is of the form [0,0,...,0,x]
# with x != 0, which would correspond to an equation 0 = x != 0`
# which would make the result of `systemSolution` be Nothing automatically,
# thanks to the magic of the type `Maybe`!
#
# the constructor `maybeSystem` will be called at each step of the
# algorithm, ensuring that if at any point, the system is found unsolvable,
# no further operation will be performed.

#   maybeSystem : List (Rows n) . List (Rows n) -> Maybe (System n) [!]
def maybeSystem(pivotalLines, nonPivotalLines):
    if forall(pivotalLines + nonPivotalLines, isValidLine):
        return Maybe(value = System(pivotalLines, nonPivotalLines))
    else: return Nothing

# returns True if and only if the list
# is not a series of zeroes ended with one
# last non-zero value, as it would amount to
# an equation of the form 0 = x != 0
#
#   isValidLine : List n -> Bool [!]
def isValidLine(line):
    if len(allLines) <= 1:
        error(isValidLine, "input list is too short to be part of a `System n`")
    leftSide = line[:-1]
    rightSide = line[-1]
    if forall(leftSide, isZero):
        return isZero(rightSide)
    else:
        return True

# (you'll notice i grew tired of mentioning the ever-present
# type class [Num n] of the parameter `n`...)
            

# ==== small interlude to introduce the type/class `System n`:

# class representing a system in the process of being solved.
# mostly just contains two attributes, `pivotalLines` and
# `nonPivotalLines`, each one being a list of vectors/lines.
#
# we'll search new pivots in the nonPivotalLines list, and
# everytime we find a new pivot in a column, we'll move the corresponding
# line to the group of the "pivotalLines".
class System():
    # System : List (Row n) . List (Row n) -> System n [!]
    def __init__(self, pivotalLines, nonPivotalLines):
        self.pivotalLines = pivotalLines
        self.nonPivotalLines = nonPivotalLines
        
        allLines = pivotalLines + nonPivotalLines
        if len(allLines) == 0:
            error(System.__init__, "wrong input (two empty lists) "
                            + "for System constructor")
        self.leftSideWidth = len(allLines[0]) - 1
        # number of columns of the leftside matrix of the equation.
        # -1 because the last element of each line is 
        # part of the right side (the vector Y in AX = Y)
        # this value will be used to avoid trying to find
        # a pivot in the right side column vector


# ==== next step of the algorithm:
#
# back in `systemSolution`, with `Maybe` a valid system. If it is so,
# the method `maybeDo` will call
#     echelonized : System n . Index -> Maybe (System n)
# with this valid system as its first argument, and an additional parameter
# `colIndex = 0`.
# this function returns either `Just` an echelonized system,
# or Nothing if at some point we encounter `0 = x != 0`.
#
# this function is recursive (indirectly). colIndex represents an index of
# the column of the leftside matrix `A` in which we'll try
# to find a pivot. the recursion will thus go through each column index
# between 0 and `ncols(A)`.

#   echelonized : System n . Index -> Maybe (System n) [!]
def echelonized(system, colIndex):
    #print "DBG"
    #printMatrix(system.pivotalLines)
    #print "ùùù"
    #printMatrix(system.nonPivotalLines)
    #print "¨¨¨"
    maybePivotalLineIndex = findPivot(system, colIndex)
    if maybePivotalLineIndex != Nothing:
        # pivot not found => this column is filled with zeroes
        # on the non pivotal lines, so we do nothing
        maybeSystem = Just(system)
    else:
        pivotalLineIndex = maybePivotalLineIndex.justValue()
        maybeSystem = usePivot(system, pivotalLineIndex, colIndex)
    if maybeSystem == Nothing:
        return Nothing
    else:
        newSystem = maybeSystem.justValue()
        if colIndex >= newSystem.leftSideWidth - 1:
            # we reached the end of recursion, having
            # walked through all the columns of the leftside
            # matrix of the equation
            return Just(newSystem)
        else:
            # we repeat the process for the next column
            return echelonized(newSystem, colIndex + 1)

# the previous function starts by calling
#    findPivot : System n . Index -> Maybe Index
# which `Maybe` returns the index of the first non-pivotal line
# (that is the line which wasn't used previously for the pivot
# of another column) which
# contains a non-null element at the index column `colIndex`.
# returns Nothing if the whole column at that index is null.

# that line index depends on the number of lines in system.nonPivotalLines,
# but that's not a problem because we'll use that index only
# to isolate the line into which the pivot was found from the aforementioned list. 
 
#   findPivot : System n . Index -> Maybe Index
def findPivot(system, colIndex):
    col = columnAt(system.nonPivotalLines, colIndex)
    lineIndex = firstIndex(isNotZero, col)
    #print "findPivot", x, colIndex
    return lineIndex

# ==== next step:
# back in `echelonized`: if the index of the line of the pivot
# given by `findPivot` is Nothing, we do nothing with the system
# else, we call `usePivot` with the index of the soon-to-be pivotal line
#   usePivot : System n . Index . Index -> Maybe (System n)
#
# in usePivot: we start by isolating the new pivotal lines
# from the rest of the still-not-yet pivotal lines.
# then we recuperate the value of the pivot, using the
# index of the column we're operating over.
#
# we create a function which will be used over all the lines
# in `system`, both the pivotal ones and the non pivotal ones,
# except the one that was just isolated, the one that contains
# the pivot.
#
# the operation consists in creating zeroes everywhere in the column
# except for the pivot. the core of the process is in the function
# `modifiedLine` (i know, the name is not very appropriate... it's
# the best i found though).

#   usePivot : System n . Index . Index -> Maybe (System n) [!]
def usePivot(system, pivotalLineIndex, colIndex):
    (pivotalLine, nonPivotalLines) = \
        isolateItem(system.nonPivotalLines, pivotalLineIndex)
    pivot = pivotalLine[colIndex]
    #print "pivot", pivot
    def forEachLine(line):
        val = line[colIndex]
        coeff = val / pivot # that way, val - coeff * pivot == 0
        return modifiedLine(line, pivotalLine, coeff)
    newPivotalLines = map(forEachLine, system.pivotalLines) + [pivotalLine]
    newNonPivotalLines = map(forEachLine, nonPivotalLines)
    return maybeSystem(newPivotalLines, newNonPivotalLines)

# the function `modifiedLine` is straightforward:
# subtract each value of `line` by the multiplication
# of an appropriate coefficient with each value of
# `otherLine`.
# the appropriate coefficient is calculated so
# that the element at the column of the current pivot
# in the `line` become zero (cf `forEachLine` in usePivot)

#   modifiedLine : List n . List n . n -> List n
def modifiedLine(line, otherLine, coeff):
    def f(val, otherVal):
        return val - otherVal * coeff
    return zipWith(f, line, otherLine)

# ==== next step
# back in usePivot:
# as previously mentioned, we used forEachLine over both
# the pivotal and non pivotal lines, except the currently
# pivotal line (the one one which we found the pivot we're
# actually using).
#
# from then on, we `Maybe` build a new system, not forgetting
# to stash the latest pivotal lines with all the old pivotal lines
#
# maybeSystem will thereafter test that no line is invalid (0 = x != 0).

# ==== next step
# back to echelonized: we get back the result of usePivot. if Nothing,
# we return Nothing and therefore break the recursion. if not,
# we check if we're at the last column of the matrix A in AX = Y, and
# if so, we return the result of usePivot and break the recursion.
# if not, we call `echelonized` recursively again with the justValue() of
# the result of `usePivot`, and an incremented column index.

# i deem the recursion acceptable even in Python because
# nobody will ever use this program to solve a system
# of several hundreds of variables, will they?

# ==== next step:
# we exited `echelonized`, so we're back in `systemSolution`, with either
# Nothing (in which case we directly return Nothing)
# or with `Just` an echelonized system.
# in which case: we have to take care of an extreme, special case:
# when both sides of the equation are null (a null matrix and vector).
# cf the body of `systemSolution` for more details.
#
# from now on we'll assume the leftside is not a null matrix,
# and therefore we at least found one pivot.
# we call keepPivotalLines over the echelonized system.
#   keepPivotalLines : System n -> List (Row n) [!]
#
# this function is extremely short and nearly useless, but is standing alone
# for the sake of clarity. its purpose is to mark the moment when
# we throw away the remaining nonPivotalLines, because they're
# necessarily just full of zeroes (otherwise they'd either be invalid,
# or would imply the Gauss Algorithm implemented here utterly failed somehow
# along the way).
# this, of course, should never happen.
# the result of keepPivotalLines is thus `system.pivotalLines : List (Row n)`

#   keepPivotalLines : System n -> List (Row n) [!]
def keepPivotalLines(system):
    if not forall(system.nonPivotalLines, isNullVector):
        error(keepPivotalLines, "somehow after successfully echelonizing, "
                    + "one non pivotal line is not full of zeroes")
    return system.pivotalLines

# ==== next step:
# once keepPivotalLines has been called, it's the turn of
#   normalized : List (Row n) -> List (Row n)
# whose job is to normalize each pivotal line, aka to
# multiply each pivotal line by a coefficient
# so that each pivot (which is also the first non-zero value
# on each line) take the value of 1.

#   normalized : List (Row n) -> List (Row n)
def normalized(pivotalLines):
    return normalizedPivotalLines = map(normalizedLine, system.pivotalLines)

# normalized delegates all the work to map and to:
#   normalizedLine : Row n -> Row n
# which replaces each value in the input
# with itself divided by the pivot, which
# is always the first non-zero value
# encountered in the list.

#   normalizedLine : Row n -> Row n [!]
def normalizedLine(line):
    maybePivotIx = firstIndex(isNotZero, line)
    if maybePivotIx == Nothing:
        # the line is full of zeroes:
        # should never happen
        error(normalizedLine, "the line is full of zeroes")
    
    pivot = line[maybePivotIx.justValue()]
    if pivot != 1:
        return map(lambda val: val / pivot, line)
    else:
        return line

# ==== next step:
# now's the time to extract the solution from
# the normalized pivotal lines.
#     extractSolution : List (Row n) -> Solution n
# let us be reminded that:
#     Solution n = (Maybe (Family n), Vector n)
# that is, a solution is the couple composed of `Maybe`
# the kernel basis, or Nothing if the kernel is {0}
# and of the particular solution to the system.
#
# it's the trickiest part of the algorithm.
#
# we start by ungluing the leftside and rightside of
# each line, to recuperate a left matrix and right vector.
#
# we obtain `p = ncols(leftMatrix)`,
# then we get the column indices of each pivot in each pivotal line
# (that will be the first non null value of each line).
# we use it to get the column indices which *don't* contain
# any pivot, with the help of `substractLists`.
#
# we then negate all the elements of the left matrix.
# it also negates the (normalized) pivots but we don't
# care because they'll soon be thrown away anyway.
#
# for each non pivotal column index:
# we build a unit vector with a `1` at that
# column index, with `p` coordinates.
# we then insert that vector inside the left Matrix
# and we of course insert a corresponding 0 in the
# right side vector.
#
# this finally done, we only need to get the columns
# of the left side matrix, eliminate the columns of the
# pivots, and we get the basis of the kernel.
#
# the particular solution is just the right side vector.
# we re

#     extractSolution : List (Row n) -> Solution n
def extractSolution(lines):
    (leftMatrix, rightVector) = unzipWith(splitSides, lines)
    p = ncols(leftMatrix)
    pivotalColIs = firstNonNullEachLine(leftMatrix)
    nonPivotalColIs = subtractLists(range(p), pivotalColIs)
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

def splitSides(line):
    leftSide = line[:-1]
    rightSide = line[-1]
    return (leftSide, rightSide)


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
