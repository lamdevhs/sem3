from Either import Left, Right, eitherSequence
from Parsing import noise
from List import grouped
from Matrix import matrixFromList
from Symbols import noSolutionSymbol, nullVecSpaceSymbol

from FracCompat import Fraction, isFraction



def parseFilePart3(allLines):
    groupSize = 5
    filteredLines = filterOut(noise, allLines)
    return parseByGroup(filteredLines, groupSize, parseGroup)

def parseGroup(tup):
    def Error(index, message):
        return Left("system #" + str(index) + ": " + message)    
    
    (lines, index) = tup
    one = lines[0].split()
    two = lines[1].split()
    
    if len(one) == 0 or len(two) == 0:
        return Error(index, "lines 1 or 2 empty")
    
    if not forall(one + two, isFraction):
        return Error(index, "a token on line #1 or #2 is not a valid fractional number")
    
    n = len(two)
    np = len(one)
    if np % n != 0:
        return Error(index, "number of tokens on line #2 is not multiple of number of tokens on #1")
    
    p = np / p
    
    if lines[2] != noSolutionSymbol and lines[3] != noSolutionSymbol:
        three = lines[2].split()
        if lines[3] == nullVecSpaceSymbol:
            kerBase = []
        else:
	    four = lines[3].split()
	    if len(three) != p:
	        return Error(index, "line #3 is the wrong size for being a particular solution")
    
	    pq = len(four)
	    if pq % p != 0:
	        return Error(index, "number of tokens on line #4 is not multiple of number of token on #3")
    	
	    kerDim = pq / p
            kerBase = grouped(map(Fraction, four), kerDim)
	
        pSol = map(Fraction, three)
        maybeSolution = Just((kerBase, pSol))
    elif lines[2] == "NOTHING" and lines[3] == "NOTHING":
        maybeSolution = Nothing
    else:
        return Error(index, "lines #3 and #4 are invalid, somehow")
    
    rightSide = map(Fraction, one)
    leftSide = matrixFromList(map(Fraction, two), n, p)
    system = (leftSide, rightSide)
    
    out = (system, maybeSolution)
    return Right(out)