from Either import Left, Right
from Maybe import Just, Nothing
from Bool import forall
from Parsing import noise, parseByGroup
from List import grouped, filterOut, bimap
from Matrix import matrixFromList
from Symbols import noSolutionSymbol, nullVecSpaceSymbol


# `fractionMaker is there due to compatibility
# issues between Python's Fraction and Sage's Rational
# cf PDF for more information.

# parseFilePart3 is the parser for part 3.
# its input format is consistent with the serializing
# function `sysAndSolToString` (in `Part2.py`).
#
# it first eliminates empty lines and comments
# then it uses `parseByGroup` (in Parsing.py)
# to get `Either` a list of parsed (system, solution)s
# (as lists of tuples of pythonic (raw) matrices and vectors,
# that is, they aren't *sage* matrices and vectors, just lists
# of lists of fractions).
# or an error message if the format of the content
# if the file isn't `Right`.

# we define first:
# RawSystem = (Matrix Fraction, Vector Fraction) -- leftside, rightside
# RawSolution = (Family Fraction, Vector Fraction) -- basis and particular solution
#
# note: Lines = List String
#
#   parseFilePart3 : (String -> Fraction) -- fractionMaker
#                   -> (Lines -> Either String (RawSystem, Maybe RawSolution))
def parseFilePart3(fractionMaker):
    def _parseFilePart3(allLines):
        groupSize = 4
        filteredLines = filterOut(noise, allLines)
        return parseByGroup(filteredLines, groupSize, parseGroup(fractionMaker))
    return _parseFilePart3



# ==== the parsing of each group works as follows:
# first, we get the tokens of lines 1 and 2, and
# we strip of whitespace the lines 3 and 4.
# we don't split those ones till later because
# they could contain symbols: strings representing
# no solution, or representing a kernel reduced
# to the null vector. (cf Symbols.py)
#
# we test if lines 1 or 2 are empty (which shouldn't ever happen)
# we test if all tokens on those lines represent proper fractions

# if all is good, we get the length of the first line `n`, which
# represents the right side vector of the equation.
# it's also the number of lines of the `np`-sized leftside matrix.
#
# `np` must be the amount of tokens on line 2, which represent said
# leftside matrix. we check p is therefore a multiple of np.
#
# we recuperate p (the number of columns of the leftside matrix)
# by dividing np with n.
#
# back to lines 3 and 4, meant to contain respectively the particular
# solution and the kernel basis found.
# if both only contain the token "NoSolution", it means
# the system was found unsolvable, and therefore we'll return Nothing
# as value of type `Maybe RawSolution`.
#
# if they don't, we check if line 3 contains fractions only.
# 
# then we check if line 4 contains the symbol "NullVecSpace",
# which represents a kernel reduced to {0}.
# if so, the kernel basis will be `[] : Family Fraction`.
#
# else, we get the size of the particular solution (line 3):
# it should be the size of each vector of the kernel basis (we check that too)
#
# we finally transform each token into a fraction with fractionMaker,
# then we build our matrices and families and vectors and then our tuples
# then finally all of it is wrapped into the constructor `Right`.

#   parseGroup : (String -> Fraction) -- fractionMaker
#              -> type of `_parseGroup` -- cf below
def parseGroup(fractionMaker):
    def isFraction(token):
        try:
            fractionMaker(token)
            return True
        except:
            return False

    #   _parseGroup : (Lines, Index) -> Either String (RawSystem, Maybe RawSolution)
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
            return Error(index, "at least one token on line #1 or #2 is not a valid fractional number")

        n = len(one)
        np = len(two)
        if np % n != 0:
            return Error(index, "number of tokens on line #2 is not multiple of number of tokens on #1")

        p = np / n

        if line3 != noSolutionSymbol and line4 != noSolutionSymbol:
            three = lines[2].split()
            if not forall(three, isFraction):
                return Error(index, "at least one token on line #3 is not a valid fractional number")

            if len(three) != p:
                return Error(index, "line #3 is the wrong size for being a particular solution")
            pSol = map(fractionMaker, three)
            if line4 == nullVecSpaceSymbol:
                kerBase = []
            else:
                four = line4.split()
                if not forall(four, isFraction):
                    return Error(index, "at least one token on line #4 is not a valid fractional number")
                
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