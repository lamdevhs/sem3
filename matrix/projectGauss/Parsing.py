# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: Parsing
Description: tools to parse files containing linear systems.
"""

from fractions import Fraction

from Bool import anyTrue, forall
from Matrix import matrixFromList
from Either import Left, Right, eitherSequence
from List import filterOut, grouped

def isComment(line):
    sline = line.lstrip()
    if len(sline) == 0:
        return False
    return sline[0] == '#'

def isEmpty(line):
    return line.lstrip() == ""


noise = anyTrue(isComment, isEmpty)            

def isFraction(token):
    try:
        Fraction(token)
        return True
    except:
        return False

def isNat(token):
    return token.isdigit()


def parseGroup(tup):
    def Error(index, message):
        return Left("group #" + str(index) + ": " + message)    
    
    (group, index) = tup
    one = group[0].split()
    two = group[1].split()
    three = group[2].split()
    four = group[3].split()
    
    if len(one) != 1 or len(two) != 1 or len(three) == 0 or len(four) == 0:
        return Error(index, "lines 1 or 2 too long, or lines 3 or 4 empty")
    
    if not isNat(one[0]) or not isNat(two[0]):
        return Error(index, "line 1 or 2 does not contain a natural integer")
    lineNumber = int(one[0])
    varNumber = int(two[0])
    if lineNumber == 0 or varNumber == 0:
        return Error(index, "line 1 or 2 does not contain a non-zero natural integer")
    
    if len(three) != lineNumber * varNumber or len(four) != lineNumber:
        return Error(index, "length of line 3 or 4 don't match values of lines 1 and 2")
    if not forall(three + four, isFraction):
        return Error(index, "at least one token on line 3 or 4 is not a valid fraction")
    
    leftSideMatrix = matrixFromList(map(Fraction, three), lineNumber, varNumber)
    rightSideVector = map(Fraction, four)
    out = (leftSideMatrix, rightSideVector)
    return Right(out)


def parseFile(allLines):
    lines = filterOut(noise, allLines)
    if len(lines) == 0 or len(lines) % 4 != 0:
        return Left("file has number of lines null or not multiple of 4")
    groups = grouped(lines, 4)
    groupIndexes = range(len(groups))
    return eitherSequence(parseGroup, zip(groups, groupIndexes))
