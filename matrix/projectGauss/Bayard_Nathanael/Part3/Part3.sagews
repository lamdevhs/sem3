︠ee65c268-51fc-432c-962f-0f3d461d2ff7r︠
from ParsingPart3 import parseFilePart3
from Maybe import Just, Nothing
from List import bimap
from UI import prompt

# entry point for part 3
# cf UI.py/prompt for clarifications
# and also the PDF
#
#   promptPart3 : Void -> Void [IO]
def promptPart3():
    prompt(title = "Part 3: Checking unicity of solutions found",
           request = "Enter filepath of file containing the systems and their solutions. "
             + "(they should be called test1.solutions and test2.solutions.)",
           parser = parseFilePart3(fractionMaker = Rational),
           callback = checker,
           getInput = getInput)

# cf PDF, relative to compatibility issues
# between Sage and Python code
#
#   getInput : Void -> String [IO]
def getInput():
    out = raw_input()
    return out

# gets the result of the parsing by ParsingPart3/parseFilePart3
# and checks the solutions found by python with sage's.
# if checkingSolution has only returned True for each system
# then all is ok and we tell the user just that.
#
#   checker : List (RawSystem n, RawSolution n) . String -> Void [IO]
def checker(rawSystemsAndSolutions, filepath):
    results = bimap(checkingSolution, rawSystemsAndSolutions)
    if forall(results, lambda bool: bool == True):
        show("all solutions were found consistent between python and sage.")
    show("no more systems/solutions in this file.")

# (this comes directly from Part2.py)
# transforms lists of numbers into
# Sage matrices and vectors
# in other terms, "bakes" raw systems
# into something that sage can use.
#
#   bakedSystem : Matrix n . Vector n -> (SageMatrix n, SageVector n)
def bakedSystem(rawMatrix, rawVector):
    return (matrix(QQ, rawMatrix), vector(QQ, rawVector))

# (this comes directly from Part2.py)
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

# the function that checks and reports each system in isolation.
# follows the principles described in the PDF
# returns a boolean describing if an inconsistency was
# found for the given system.
#
#   checkingSolution : RawSystem n . Maybe (RawSolution n) -> Bool [IO]
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
    
    if pyKernel != sageKernel or len(pyKBasis) != sageKernel.dimension():
        sayInconsistency()
        show("the kernels found by python and sage and different, "
             + "or maybe the family found by python is not a base (too many vectors).")
    
    testPSol = leftSide * vec2Matrix(pyPSol)
    if testPSol != vec2Matrix(rightSide):
        show(testPSol)
        sayInconsistency()
        show("the particular solution found by python is not valid.")
    
    return True

#   vec2Matrix : SageVector n -> SageMatrix n
def vec2Matrix(vec):
    return matrix(QQ, vec).transpose()

# the origin is either "Python" or "Sage"
#
#   showSolution : String, Maybe (Solution) -> Void [IO]
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

︡c0ed652f-7a10-4705-826e-2321e7c9b11a︡{"stdout":"Part 3: Checking unicity of solutions found\n\n\nEnter filepath of file containing the systems and their solutions. (they should be called test1.solutions and test2.solutions.) (Type `:q` to quit.)\n"}︡{"raw_input":{"prompt":""}}︡{"delete_last":true}︡{"raw_input":{"prompt":"","submitted":true,"value":"test1.solutions"}}︡{"stdout":"File parsed successfully."}︡{"stdout":"\n"}︡{"html":"<div align='center'>all solutions were found consistent between python and sage.</div>"}︡{"html":"<div align='center'>no more systems/solutions in this file.</div>"}︡{"stdout":"\n\nEnter filepath of file containing the systems and their solutions. (they should be called test1.solutions and test2.solutions.) (Type `:q` to quit.)\n"}︡{"raw_input":{"prompt":""}}︡{"delete_last":true}︡{"raw_input":{"prompt":"","submitted":true,"value":"test2.solutions"}}︡{"stdout":"File parsed successfully."}︡{"stdout":"\n"}︡{"html":"<div align='center'>all solutions were found consistent between python and sage.</div>"}︡{"html":"<div align='center'>no more systems/solutions in this file.</div>"}︡{"stdout":"\n\nEnter filepath of file containing the systems and their solutions. (they should be called test1.solutions and test2.solutions.) (Type `:q` to quit.)\n"}︡{"raw_input":{"prompt":""}}









