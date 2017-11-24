from lib.Bool import forall
from lib.Matrix import matrixFromList
from lib.Either import Left, Right
from lib.List import filterOut
from lib.Parsing import noise, parseByGroup, isNat

__SAGE__ = False

if __SAGE__:
    def Fraction(x):
        return Rational(x)
    
    def isFraction(token):
        try:
            Rational(token)
            return True
        except:
            return False
else:
    from fractions import Fraction
    def isFraction(token):
        try:
            Fraction(token)
            return True
        except:
            return False

def parseGroup(fractionMaker):
    def _parseGroup(tup):
        def Error(index, message):
	    return Left("system #" + str(index) + ": " + message)    
    
        (group, index) = tup
        one = group[0].split()
        two = group[1].split()
        three = group[2].split()
        four = group[3].split()
        
        if len(one) != 1 or len(two) != 1 or len(three) == 0 or len(four) == 0:
            return Error(index, "lines 1 or 2 too long, or lines 3 or 4 empty")
   
        if not isNat(one[0]) or not isNat(two[0]):
            return Error(index, "line 1 or 2 does not contain a natural integer")
        lineNumber = int(one[0])
        varNumber = int(two[0])
        if lineNumber == 0 or varNumber == 0:
            return Error(index, "line 1 or 2 does not contain a non-zero natural integer")
    
        if len(three) != lineNumber * varNumber or len(four) != lineNumber:
            return Error(index, "length of line 3 or 4 don't match values of lines 1 and 2")
        if not forall(three + four, isFraction):
            return Error(index, "at least one token on line 3 or 4 is not a valid fraction")
    
        leftSideMatrix = matrixFromList(map(fractionMaker, three), lineNumber, varNumber)
        rightSideVector = map(fractionMaker, four)
        out = (leftSideMatrix, rightSideVector)
        return Right(out)
    return _parseGroup


def parseFilePart12(fractionMaker):
    def _parseFilePart12(allLines):
        groupSize = 4
        filteredLines = filterOut(noise, allLines)
        return parseByGroup(filteredLines, groupSize, parseGroup(fractionMaker))
    return _parseFilePart12
