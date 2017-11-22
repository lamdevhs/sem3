# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: Main
Description: 
"""
import os 
workingDir = os.path.dirname(os.path.realpath(__file__))

from Parsing import parseFile, gaussMethod
from List import toPrettyStringLL, toPrettyString, flatten, asLines
from Either import Left
from Matrix import matrixOfFamily

# TODO:
# pdf
# commentaires + sig

# sage part 1

# store answers for part 3
# parse answers in sage for part 3 


def systemsFromFile(filepath):
    try:
        desc= open(filepath,'rt')
        allLines = desc.readlines()
        desc.close()
    except:
        return Left("error while trying to read file. probably wrong path")
    return parseFile(allLines)

def solveSystemsFromFile(filepath):
    result = systemsFromFile(filepath)
    if result.isLeft:
        print 'Error for filepath "' + filepath + '": ' + result.leftValue
        print "---> abandoning"
        return
    print "File parsed successfully."
    systems = result.rightValue
    for system in systems:
        (leftSide, rightSide) = system
        print "-----------------------"
        print "leftside matrix:"
        print toPrettyStringLL(leftSide)
        print "rightSide vector:"
        print toPrettyString(rightSide)
        result = gaussMethod(*system)
        if result.isNothing():
            print "system was found unsolvable. the solution space is the empty set"
            continue
        (kernelBasis, pSolution) = result.value
        if kernelBasis == []:
            print "kernel of left matrix is reduced to {vector null}."
        else:
            print "basis of kernel of left matrix:"
            toPrettyStringLL(matrixOfFamily(kernelBasis))
        print "particular solution:"
        print toPrettyString(pSolution)
        
    print "no more systems in this file."

def main():
    print "Interactive linear system solver. Type --quit to quit."
    while True:
        print "\n\nfilepath of file containing the systems to solve: ",
        filepath = raw_input()
        if filepath == "--quit":
            break
        solveSystemsFromFile(workingDir + "/" + filepath)
    print "quitting."

main()


def solutionsToString(affine, leftSide, rightSide):
    (kerBasis, pSol) = affine
    out = [toPrettyString(rightSide),
           toPrettyString(flatten(leftSide)),
           toPrettyString(pSol),
           toPrettyString(flatten(kerBasis))]
    return asLines(out)

def systemsToFile(filepath, solutions, systems):
    try:
        desc= open(filepath,'rt')
        allLines = desc.readlines()
        desc.close()
    except:
        return Left("error while trying to read file. probably wrong path")
    return parseFile(allLines)