# -*- coding: utf-8 -*-
import os 

from Parsing import parseFile
from System import systemSolution
from List import toPrettyStringLL, toPrettyString, flatten, asLines
from Either import Left
from Matrix import matrixOfFamily

workingDir = os.path.dirname(os.path.realpath(__file__))

# TODO:
# pdf
# commentaires + sig

# sage part 1

# store answers for part 3
# parse answers in sage for part 3 


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
        toPrettyStringLL(matrixOfFamily(kernelBasis))
    print "particular solution:"
    print toPrettyString(pSolution)

def main():
    print "Interactive linear system solver. Type --quit to quit."
    while True:
        print "\n\nEnter filepath of file containing the systems to solve: ",
        filepath = raw_input()
        if filepath == "--quit":
            break
        parsingResult = systemsFromFile(filepath)
        if parsingResult.isLeft:
            print 'Error while parsing file "' + filepath + '": ' + parsingResult.leftValue
            print "---> abandoning"
            continue
        print "File parsed successfully."
        systems = parsingResult.rightValue
        sysAndSolutions = zip(systems, map(tupled(systemSolution), systems))
        map(tupled(printResult), sysAndSolutions)
        print "no more systems in this file."
        solFilepath = workingDir + "/" + filepath + ".solutions"
        report = saveSolutionsToFile(solFilepath, sysAndSolutions)
        print report

    print "quitting."

main()

def saveSolutionsToFile(filepath, sysAndSolutions):
    toWrite = asLines(map(tupled(sysAndSolToString), sysAndSolutions))
    return writeToFile(filepath, toWrite)

def writeToFile(filepath, toWrite):
    try:
        with open(filepath,'w') as desc:
           desc.write(toWrite)
        return 'solutions successfully saved to file "' + filepath + '".'
    except:
        return 'error while trying to write into file "' + filepath + '".'

def sysAndSolToString(system, solution):
    (leftSide, rightSide) = system
    out = [toPrettyString(rightSide),
           toPrettyString(flatten(leftSide))]

    if solution.isNothing():
        out += ["NOTHING", "NOTHING", ""]
    else: 
        (kerBasis, pSol) = solution
        out += [toPrettyString(pSol),
                toPrettyString(flatten(kerBasis)), ""]
    return asLines(out)

