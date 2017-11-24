from lib.UI import prompt
from lib.List import toPrettyStringLL, toPrettyString, flatten, asLines, asWords, bimap
from lib.System import systemSolution
from lib.Matrix import matrixOfFamily
from lib.Symbols import noSolutionSymbol, nullVecSpaceSymbol

from ParsingPart12 import parseFilePart12

from fractions import Fraction

import os
workingDir = os.path.dirname(os.path.realpath(__file__))


def promptPart2():
    prompt(title = "Part 2: Interactive linear system solver.",
           request = "Enter filepath of file containing the systems to solve.",
           parser = parseFilePart12(fractionMaker = Fraction),
           callback = solver,
           getInput = getInput)

# for keeping compatibility with Sage, cf function 'UI.prompt'
def getInput():
    out = raw_input()
    return out


def solver(systems, filepath):
    solutions = bimap(systemSolution, systems)
    sysAndSolutions = zip(systems, solutions)
    bimap(printResult, sysAndSolutions)
    print "no more systems in this file."
    solFilepath = workingDir + "/" + filepath + ".solutions"
    report = saveSolutionsToFile(solFilepath, sysAndSolutions)
    print report
    return


def printResult(system, solution):
    (leftSide, rightSide) = system
    print "\n-----------------------"
    print "leftside matrix:"
    print toPrettyStringLL(leftSide)
    print "rightSide vector:"
    print toPrettyString(rightSide)
    if solution.isNothing():
        print "system was found unsolvable. the solution space is the empty set"
        return
    (kernelBasis, pSolution) = solution.value
    if kernelBasis == []:
        print "kernel of left matrix is reduced to {vector null}."
    else:
        print "basis of kernel of left matrix:"
        print toPrettyStringLL(matrixOfFamily(kernelBasis))
    print "particular solution:"
    print toPrettyString(pSolution)


def saveSolutionsToFile(filepath, sysAndSolutions):
    toWrite = asLines(bimap(sysAndSolToString, sysAndSolutions))
    return writeToFile(filepath, toWrite)

def writeToFile(filepath, toWrite):
    try:
        with open(filepath,'w') as desc:
           desc.write(toWrite + "\n")
        return 'solutions successfully saved to file "' + filepath + '".'
    except:
        return 'error while trying to write into file "' + filepath + '".'

def sysAndSolToString(system, solution):
    (leftSide, rightSide) = system
    out = ["#", asWords(rightSide),
           asWords(flatten(leftSide))]

    if solution.isNothing():
        out += [noSolutionSymbol, noSolutionSymbol]
    else:
        (kerBasis, pSol) = solution.value
        if kerBasis == []:
            kerStr = nullVecSpaceSymbol
        else:
            kerStr = asWords(flatten(kerBasis))
        out += [asWords(pSol), kerStr]
    return asLines(out)


if __name__ == "__main__":
    promptPart2()