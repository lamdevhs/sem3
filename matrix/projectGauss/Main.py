# -*- coding: utf-8 -*-
import os 

from Parsing import parseFile
from System import systemSolution
from List import toPrettyStringLL, toPrettyString, flatten, asLines, asWords, tupled
from Either import Left
from Matrix import matrixOfFamily

workingDir = os.path.dirname(os.path.realpath(__file__))

# TODO:
# pdf
# commentaires + sig

# sage part 1

# store answers for part 3
# parse answers in sage for part 3 

# separate equation from system (mention it in pdf)
# write bimap, erase tupled
# add variadic notation in pdf

def prompt(handler):
    print "Interactive linear system solver. Type `:q` to quit."
    while True:
        print "\n\nEnter filepath of file containing the systems to solve: ",
        filepath = raw_input()
        if filepath == ":q":
            break
    	parsingResult = systemsFromFile(filepath)
        if parsingResult.isLeft:
            print 'Error while parsing file "' + filepath + '": ' + parsingResult.leftValue
            print "---> abandoning"
            return
        print "File parsed successfully."
        handler(parsingResult.rightValue)
    print "quitting."

def withSystems(systems):
    solutions = map(tupled(systemSolution), systems)
    sysAndSolutions = zip(systems, solutions)
    map(tupled(printResult), sysAndSolutions)
    print "no more systems in this file."
    solFilepath = workingDir + "/" + filepath + ".solutions"
    report = saveSolutionsToFile(solFilepath, sysAndSolutions)
    print report
    return


def systemsFromFile(filepath):
    try:
        with open(filepath,'rt') as desc:
          allLines = desc.readlines()
    except:
        return Left("error while trying to read file. probably wrong path")
    return parseFile(allLines)

def printResult(system, solution):
    (leftSide, rightSide) = system
    print "-----------------------"
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
    toWrite = asLines(map(tupled(sysAndSolToString), sysAndSolutions))
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
        out += ["NOTHING", "NOTHING"]
    else: 
        (kerBasis, pSol) = solution.value
        out += [asWords(pSol),
                asWords(flatten(kerBasis))]
    return asLines(out)

if __name__ == "__main__":
    prompt(withSystems)

