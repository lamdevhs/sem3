from ParsingPart3 import parseFilePart3
from Maybe import Just, Nothing
from List import bimap
from UI import prompt

def promptPart3():
    prompt(title = "Part 3: Checking unicity of solutions found",
           request = "Enter filepath of file containing the systems and their solutions. "
             + "(they should be called test1.solutions and test2.solutions.)",
           parser = parseFilePart3(fractionMaker = Rational),
           callback = checker,
           getInput = getInput)

def getInput():
    out = raw_input()
    return out

def checker(rawSystemsAndSolutions, filepath):
    results = bimap(checkingSolution, rawSystemsAndSolutions)
    if forall(results, lambda bool: bool == True):
        show("all solutions were found consistent between python and sage.")
    print "no more systems/solutions in this file."

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

def checkingSolution(rawSystem, pySolution):
    (rawLeftSide, rawVector) = rawSystem
    leftSide = matrix(QQ, rawLeftSide)
    rightSide = vector(QQ, rawVector)

    sageSolution = systemSolution(leftSide, rightSide)
    
    def sayInconsistency():
        show("-----------------------------")
        show("an inconsistency was found:")
        show("leftside matrix:")
        show(leftSide)
        show("rightSide vector:")
        show(rightSide)
        showSolution("sage", sageSolution)
        showSolution("python", pySolution)
    
    
    if pySolution == Nothing:
        if Nothing == sageSolution:
            return True
        else:
            sayInconsistency()
            return False
    if sageSolution == Nothing:
        sayInconsistency()
        return False
    
    (sageKBasis, sagePSol) = sageSolution.justValue()
    (pyKBasis, pyPSol) = pySolution.justValue()
    
    p = len(list(sagePSol))
    domain = VectorSpace(QQ, p)
    pyKernel = domain.subspace(pyKBasis)
    sageKernel = leftSide.right_kernel()
    
    if pyKernel != sageKernel:
        sayInconsistency()
        show("the kernels found by python and sage and different.")
    
    testPSol = leftSide * vec2Matrix(pyPSol)
    if testPSol != vec2Matrix(rightSide):
        show(testPSol)
        sayInconsistency()
        show("the particular solution found by python is not valid.")
    
    return True

def vec2Matrix(vec):
    return matrix(QQ, vec).transpose()
    
def showSolution(origin, maybeSolution):
    if maybeSolution == Nothing:
        show(origin + " found the set of solutions to be empty.")
        return
    show(origin + " found the following solution set:")
    (kernelBasis, pSolution) = maybeSolution.justValue()
    if 0 == len(kernelBasis):
        show("kernel of left matrix is reduced to {vector null}.")
    else:
        show("basis of kernel of left matrix, disposed as columns of a matrix:")
        show(matrix(QQ,kernelBasis).transpose())
    show("particular solution found:")
    show(pSolution)
    
    
promptPart3()