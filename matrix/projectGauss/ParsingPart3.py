from Either import Left, Right
from Maybe import Just, Nothing
from Bool import forall
from Parsing import noise, parseByGroup
from List import grouped, filterOut, bimap
from Matrix import matrixFromList
from Symbols import noSolutionSymbol, nullVecSpaceSymbol


def parseFilePart3(fractionMaker):
    def _parseFilePart3(allLines):
        groupSize = 4
        filteredLines = filterOut(noise, allLines)
        return parseByGroup(filteredLines, groupSize, parseGroup(fractionMaker))
    return _parseFilePart3

def parseGroup(fractionMaker):
    def isFraction(token):
        try:
            fractionMaker(token)
            return True
        except:
            return False

    def _parseGroup(tup):
        def Error(index, message):
            return Left("system #" + str(index) + ": " + message)    

        (lines, index) = tup
        one = lines[0].split()
        two = lines[1].split()
        line3 = lines[2].strip()
        line4 = lines[3].strip()

        if len(one) == 0 or len(two) == 0:
            return Error(index, "lines 1 or 2 empty")

        if not forall(one + two, isFraction):
            return Error(index, "a token on line #1 or #2 is not a valid fractional number")

        n = len(one)
        np = len(two)
        if np % n != 0:
            return Error(index, "number of tokens on line #2 is not multiple of number of tokens on #1")

        p = np / n

        if line3 != noSolutionSymbol and line4 != noSolutionSymbol:
            three = lines[2].split()
            if len(three) != p:
                    return Error(index, "line #3 is the wrong size for being a particular solution")
            pSol = map(fractionMaker, three)
            if line4 == nullVecSpaceSymbol:
                kerBase = []
            else:
                four = line4.split()
                pq = len(four)
                if pq % p != 0:
                    return Error(index, "number of tokens on line #4 is not multiple of number of token on #3")

                kerBase = grouped(map(fractionMaker, four), p)
            maybeSolution = Just((kerBase, pSol))
        elif line3 == noSolutionSymbol and line4 == noSolutionSymbol:
            maybeSolution = Nothing
        else:
            return Error(index, "lines #3 and #4 are invalid, somehow")

        rightSide = map(fractionMaker, one)
        leftSide = matrixFromList(map(fractionMaker, two), n, p)
        system = (leftSide, rightSide)

        out = (system, maybeSolution)
        return Right(out)
    return _parseGroup