︠41c756b3-dbb3-46a3-93eb-71f6caaf9232s︠
from UI import prompt
from ParsingPart12 import parseFilePart12
from List import bimap

from time import sleep

from Maybe import Nothing, Just


# this is the entry point for the part 1
# cf UI.py and the PDF to understand `prompt`
# and the compatibility issues that arose from
# trying to use the same function for both Python
# and Sage.
# 
#   promptPart1 : Void -> Void [IO]
def promptPart1():
    prompt(title = "Part 1: Interactive linear system solver using Sage. Type `:q` to quit.",
           request = "Enter filepath of file containing the systems to solve: "
             + "(they should be called test0, test1 and test2.)",
           parser = parseFilePart12(fractionMaker = Rational),
           callback = solver,
           getInput = getInput)

# necessary because UI is not a sage module and therefore otherwise it crashes
# cf PDF
#   getInput : Void -> String [IO]
def getInput():
    out = raw_input()
    return out


# this one does most of the work of using Sage to solve the systems
# and print the results.
#   solver : List (RawSystem n) . String -> Void [IO]
def solver(rawSystems, filepath):
    systems = bimap(bakedSystem, rawSystems)
    solutions = bimap(systemSolution, systems)
    sysAndSolutions = zip(systems, solutions)
    bimap(printResult, sysAndSolutions)
    print "no more systems in this file."

# transforms lists of numbers into
# Sage matrices and vectors
# in other terms, "bakes" raw systems
# into something that sage can use.
#
#   bakedSystem : Matrix n . Vector n -> (SageMatrix n, SageVector n)
def bakedSystem(rawMatrix, rawVector):
    return (matrix(QQ, rawMatrix), vector(QQ, rawVector))

# returns `Just` a List of SageVectors (the kernel basis)
# and a SageVector (the particular solution)
# or Nothing if the system does not have any solution.
#
#   systemSolution : SageMatrix n . SageVector n -> Maybe (List (SageVector n), SageVector n)
def systemSolution(matrix, vector):
    kernelBasis = matrix.right_kernel().basis()
    try:
        particularSolution = matrix.solve_right(vector)
    except:
        return Nothing
    s = (kernelBasis,particularSolution)
    return Just(s)

#   printResult : SageSystem n . SageSolution -> Void []
def printResult(system, solution):
    (leftSide, rightSide) = system
    show("\n-----------------------")
    show("leftside matrix:")
    show(leftSide)
    show("rightSide vector:")
    show(rightSide)
    if solution == Nothing:
        show("system was found unsolvable. the solution space is the empty set")
        return
    (kernelBasis, pSolution) = solution.justValue()
    if 0 == len(kernelBasis):
        show("kernel of left matrix is reduced to {vector null}.")
    else:
        show("basis of kernel of left matrix, as columns of a matrix:")
        show(matrix(QQ,kernelBasis).transpose())
    show("particular solution:")
    show(pSolution)
    sleep(0.1)

promptPart1()









