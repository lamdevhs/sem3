from ParsingPart3 import parseFilePart3
from Maybe import Maybe

def getInput():
    out = raw_input()
    return out

def promptPart3():
    prompt(title = "Part 3: Checking unicity of solutions found",
           request = "Enter filepath of file containing the systems and their solutions.",
           parser = parseFilePart3,
           callback = checkPart3,
           getInput = getInput)

def checkPart3(tup):
    (system, maybeSolution) = tup
