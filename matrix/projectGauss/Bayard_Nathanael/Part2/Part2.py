from UI import prompt
from List import toPrettyStringLL, toPrettyString, flatten, asLines, asWords, bimap
from System import systemSolution
from Matrix import matrixOfFamily
from Symbols import noSolutionSymbol, nullVecSpaceSymbol
from Maybe import Just, Nothing

from ParsingPart12 import parseFilePart12

from fractions import Fraction

import os
workingDir = os.path.dirname(os.path.realpath(__file__))
    # ^--- a relative path did not work on my computer.

# the starting point of the program of part 2.
# cf UI.py/prompt to understand it better.
#
#   promptPart2 : Void -> Void [IO]
def promptPart2():
    prompt(title = "Part 2: Interactive linear system solver.",
           request = "Enter filepath of file containing the systems to solve.\n"
                   + "(they should be 'test0', 'test1' and 'test2')",
           parser = parseFilePart12(fractionMaker = Fraction),
           callback = solver,
           getInput = getInput)

# for keeping compatibility with Sage, cf function 'UI.prompt' and PDF
#
#   getInput : Void -> String [IO]
def getInput():
    out = raw_input()
    return out

# this function is called with the results of the parsing,
# and is used to both print the results of using the Gauss Method
# over the parsed systems, and to *save* those solutions with the
# systems into a file which will be used in part 3.
#
#   solver : [Num n] List (Matrix n, Vector n) . String -> Void [IO]
def solver(systems, filepath):
    solutions = bimap(systemSolution, systems)
    sysAndSolutions = zip(systems, solutions)
    bimap(printResult, sysAndSolutions)
    print "no more systems in this file."
    solFilepath = workingDir + "/" + filepath + ".solutions"
    report = saveSolutionsToFile(solFilepath, sysAndSolutions)
    print report
    return

# this one just tells what the Gauss Method found.
#
#   printResult : (Matrix n, Vector n) . Maybe (Family n, Vector n) -> Void [IO]
def printResult(system, solution):
    (leftSide, rightSide) = system
    print "\n-----------------------"
    print "leftside matrix:"
    print toPrettyStringLL(leftSide)
    print "rightSide vector:"
    print toPrettyString(rightSide)
    if solution == Nothing:
        print "system was found unsolvable. the solution space is the empty set"
        return
    (kernelBasis, pSolution) = solution.justValue()
    if 0 == len(kernelBasis):
        print "kernel of left matrix is reduced to {vector null}."
    else:
        print "basis of kernel of left matrix:"
        print toPrettyStringLL(matrixOfFamily(kernelBasis))
    print "particular solution:"
    print toPrettyString(pSolution)


# takes a list of tuples of systems and solutions, and save
# all of it to the given filepath
#
#   saveSolutionsToFile : String -- filepath
#                       . List (RawSystem n,
#                               Maybe (RawSolution n)) -- sysAndSolutions
#                       -> String -- report
#                       [IO]
def saveSolutionsToFile(filepath, sysAndSolutions):
    toWrite = asLines(bimap(sysAndSolToString, sysAndSolutions))
    return writeToFile(filepath, toWrite)


#   writeToFile : String . String -> String [IO]
def writeToFile(filepath, toWrite):
    try:
        with open(filepath,'w') as desc:
           desc.write(toWrite + "\n")
        return 'solutions successfully saved to file "' + filepath + '".'
    except:
        return 'error while trying to write into file "' + filepath + '".'


# this function does the serializing of the results of part 2
# so they can be parsed and checked in part 3.
# the format is described in the PDF and
# also in the parser for part 3 (ParsingPart3.py)
#
# sysAndSolToString : RawSystem n . Maybe (RawSolution n) -> String
def sysAndSolToString(system, solution):
    (leftSide, rightSide) = system
    out = ["#", asWords(rightSide),
           asWords(flatten(leftSide))]

    if solution == Nothing:
        out += [noSolutionSymbol, noSolutionSymbol]
    else:
        (kerBasis, pSol) = solution.justValue()
        if 0 == len(kerBasis):
            kerStr = nullVecSpaceSymbol
        else:
            kerStr = asWords(flatten(kerBasis))
        out += [asWords(pSol), kerStr]
    return asLines(out)


if __name__ == "__main__":
    promptPart2()
