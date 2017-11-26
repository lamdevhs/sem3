from Bool import forall
from Matrix import matrixFromList
from Either import Left, Right
from List import filterOut
from Parsing import noise, parseByGroup, isNat

# `fractionMaker is there due to compatibility
# issues between Python's Fraction and Sage's Rational
# cf PDF for more information.

# parseFilePart12 is the parser for both parts 1 and 2.
# it first eliminates empty lines and comments
# then it uses `parseByGroup` (in Parsing.py)
# to get `Either` a list of parsed systems
# (as lists and lists of lists)
# or an error message if the format of the content
# if the file isn't `Right` for some unfathomable reason.
#
# for each group of 4 (worthwile) lines of the input file,
# parseGroup will try to get a matrix and a right side vector.

#   parseFilePart12 : (String -> Fraction) -- fractionMaker
#                   -> (Lines -> Either String (Matrix Fraction, Vector Fraction))
def parseFilePart12(fractionMaker):
    def _parseFilePart12(allLines):
        groupSize = 4
        filteredLines = filterOut(noise, allLines)
        return parseByGroup(filteredLines, groupSize, parseGroup(fractionMaker))
    return _parseFilePart12



# ==== the parsing of each group works as follows:
# first, split each line into lists of tokens,
# each one, assumedly, being a number.
#
# test first if there's more or less than one token on
# lines 1 and 2, and if lines 3 and 4 are empty of anything
# (which should be impossible anyway).
#
# then we test if the one tokens on lines 1 and 2 are
# natural numbers with `isNat` (in Parsing.py).
#
# we recuperate the int value of each, we check if they're equal
# to 0, and then compare them with the amount of tokens on lines
# 3 and 4.
#
# if all is still ok, we check with `isFraction`
# (which depends on `fractionMaker`) if every token
# on lines 3 and 4 represent fractional numbers.
#
# if so, all that remains is to replace each line of tokens
# with a line of numbers, and use the int values of lines 1 and 2
# to build the leftside matrix from the line 3's content.
#
# we then return the tuple of the leftSide matrix and the rightSide
# vector, wrapped in a `Right` constructor, to respect the `Either` output.

#   parseGroup : (String -> Fraction) -- fractionMaker
#              -> type of `_parseGroup` -- cf below
def parseGroup(fractionMaker):
    def isFraction(token):
        try:
            fractionMaker(token)
            return True
        except:
            return False

    # note: Lines = List String
    #
    #   _parseGroup : (Lines, Index) -> Either String (Matrix Fraction, Vector Fraction)
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


