"""
Author: Nathanael Bayard
Module Name: UI
Description:
    functions used to create a minimal UI, used in common by all three parts.
    due to compatibility issues between Sage and vanilla Python, some functions
    below require as arguments some basic IO functions like 'getInput', used
    to ask the user some string as input for the program.
"""

from Either import Left, Right

# creates a basic user interface that waits for a file name,
# uses the input parser to parse it, then calls `callback` with
# the potential result.
# `title` and `request` are strings to be printed, the former once,
# the latter every time the prompt resets.
#
# there has been compatibility issues between sage and python
# (df the PDF), so i had to make `prompt` accept a function `getInput`
# to get some string typed by the user on the prompt (otherwise, Sage crashed)
#
# this function is used in all three parts.
#
# let us define the type alias:
#   Lines = List String
#
#   prompt : String -- title
#          . String -- request
#          . (Lines -> Either String b) -- parser, which may "Either-fail"
#          . (b -> Void) -- callback
#          . (Void -> String [IO]) -- getInput
#          -> Void [IO]
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
        allLines = eitherContent.rightValue
        parsingResult = parser(allLines)
        if parsingResult.isLeft:
            print 'Error while parsing file "' + filepath + '": ' + parsingResult.leftValue
            print "---> abandoning"
            continue
        print "File parsed successfully."
        callback(parsingResult.rightValue, filepath)
    print "quitting."

#   contentFromFile : String -> Either String Lines [IO]
def contentFromFile(filepath):
    try:
        with open(filepath,'rt') as desc:
          allLines = desc.readlines()
    except:
        return Left("Error while trying to read file. probably wrong path")
    return Right(allLines)
