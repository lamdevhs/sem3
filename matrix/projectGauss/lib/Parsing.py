# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: Parsing
Description: tools to parse files containing linear systems.
"""



from Either import Left, eitherSequence
from List import grouped
from Bool import anyTrue


def isComment(line):
    sline = line.lstrip()
    if len(sline) == 0:
        return False
    return sline[0] == '#'

def isEmpty(line):
    return line.lstrip() == ""


noise = anyTrue(isComment, isEmpty)            

def isNat(token):
    return token.isdigit()


def parseByGroup(lines, groupSize, groupParser):
    if len(lines) == 0 or len(lines) % groupSize != 0:
        return Left("file has number of useful lines null or not multiple of " + str(groupSize))
    groups = grouped(lines, groupSize)
    groupIndexes = range(len(groups))
    return eitherSequence(groupParser, zip(groups, groupIndexes))



    
