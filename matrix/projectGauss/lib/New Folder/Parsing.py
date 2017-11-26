"""
Author: Nathanael Bayard
Module Name: Parsing
Description: generic tools to parse files containing groups of data of same format
"""

from Either import Left, eitherMap
from List import grouped
from Bool import anyTrue


#   isComment : String -> Bool
def isComment(line):
    sline = line.lstrip()
    if len(sline) == 0:
        return False
    return sline[0] == '#'

#   isEmpty : String -> Bool
def isEmpty(line):
    return line.lstrip() == ""


# noise : String -> Bool
noise = anyTrue(isComment, isEmpty)            

# represents a natural integer: composed exclusively of characters
# representing digits 0..9. (isdigit is a built-in)
#
#   isNat : String -> Bool
def isNat(token):
    return token.isdigit()


# takes a list of lines (strings), a size of group `groupSize > 0`
# and a function that can parse a list of `groupSize` lines into some
# object of type `t`, but which may also "Either-fail".
# the parser is expected to accept tuples, with the index of the group
# as second element of the tuple, mostly for useful error-reporting.
#
# checks if the list of lines has a length multiple of the `groupSize`
# and also that `groupSize > 0`, and if not, returns `Left`, 
#
# then creates groups composed of `groupSize` lines.
#
# and then uses `mapEither`and the parser function given in input
# to parse the list of `groups` thus created.
# returns `Left` of the first failure encountered by the parser,
# or `Right` of a list of results of the parsing of each group.
#
# note: the function could actually work perfectly polymorphically
# with relation to the type `String` (but i don't use it with any
# other type and i didn't want to complicate the thing any further).
#
#   parseByGroup : List String
#                . Int
#                . ( (List String, Index) -> Either e t)
#               -> Either e (List t)
def parseByGroup(lines, groupSize, groupParser):
    if len(lines) % groupSize != 0 or groupSize == 0:
        return Left("groupSize null, or the amount of lines given is not a multiple of "
                   + "groupSize = " + str(groupSize))

    groups = grouped(lines, groupSize)

    groupIndexes = range(len(groups))
    groupAndIndexes = zip(groups, groupIndexes)
    # groupAndIndexes : List (List String, Index)

    return eitherMap(groupParser, groupAndIndexes)
