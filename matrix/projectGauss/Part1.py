︠bad85e62-bf6a-427c-8107-b14a95c31e55︠
from UI import prompt
from ParsingPart12 import parseFilePart12
from List import bimap

from Maybe import Nothing, Just

def promptPart1():
    prompt(title = "Part 1: Interactive linear system solver. Type `:q` to quit.",
           request = "Enter filepath of file containing the systems to solve:",
           parser = parseFilePart12,
           callback = solver,
           getInput = getInput)

# necessary because UI is not a sage module and therefore otherwise it crashes
def getInput():
    out = raw_input()
    return out


def solver(rawSystems, filepath):
    systems = bimap(bakedSystem, rawSystems)
    solutions = bimap(systemSolution, systems)
    sysAndSolutions = zip(systems, solutions)
    bimap(printResult, sysAndSolutions)
    print "no more systems in this file."

# transform lists of numbers into Sage
# matrices and vectors
#
def bakedSystem(rawMatrix, rawVector):
    return (matrix(QQ, rawMatrix), vector(QQ, rawVector))
    
def systemSolution(matrix, vector):
    kernelBasis = matrix.right_kernel().basis()
    try:
        particularSolution = matrix.solve_right(vector)
    except:
        return Nothing
    s = (kernelBasis,particularSolution)
    return Just(s)

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

promptPart1()









