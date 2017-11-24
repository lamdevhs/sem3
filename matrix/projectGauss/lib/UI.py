# -*- coding: utf-8 -*-
 

from Either import Left, Right



# TODO:
# pdf
# commentaires + sig

# sage part 1

# parse answers in sage for part 3

# separate equation from system (mention it in pdf)
# add variadic notation in pdf
# tell where the functions to save stuff for part 3 are in part 2 (and map of part 2 in general)


def prompt(title, request, parser, callback, getInput):
    print title
    while True:
        print "\n\n" + request + " (Type `:q` to quit.)"
        filepath = getInput()
        if filepath == ":q":
            break
    	eitherContent = contentFromFile(filepath)
        if eitherContent.isLeft:
            print eitherContent.leftValue
            print "---> abandoning"
            continue
        parsingResult = parser(eitherContent.rightValue)
        if parsingResult.isLeft:
            print 'Error while parsing file "' + filepath + '": ' + parsingResult.leftValue
            print "---> abandoning"
            continue
        print "File parsed successfully."
        callback(parsingResult.rightValue, filepath)
    print "quitting."

def contentFromFile(filepath):
    try:
        with open(filepath,'rt') as desc:
          allLines = desc.readlines()
    except:
        return Left("Error while trying to read file. probably wrong path")
    return Right(allLines)
