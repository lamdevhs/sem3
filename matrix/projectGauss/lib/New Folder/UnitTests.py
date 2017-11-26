"""
Author: Nathanael Bayard
Module Name: UnitTests
Description: module used for unit tests of the various modules of the program.
             warning: contains one instruction that actually calls a function, at
             the end of the file.
"""
from List import toPrettyStringLL

# for testing:
from unitTests.ListTests import testingList
from unitTests.BoolTests import testingBool

class Test():
    def __init__(self, functionToTest):
        self.toTest = functionToTest
        self.name = functionToTest.func_name
        self.results = []
    
    def check(self, input, output, testName = "untitled test"):
        actualOutput = self.toTest(*input)
        if actualOutput != output:
            self.results.append([testName, input, output, actualOutput])
        return self

    def checkError(self, input, testName = "untitled test"):
	try:
       	    actualOutput = self.toTest(*input)
            self.results.append([testName, input, "(error)", actualOutput])
	finally:
            return self

    def printResults(self):
        print 'unit tests for function "' + self.name + '":',
        if len(self.results) == 0:
             print "ok, all tests passed"
        else:
            print len(self.results), "tests failed:"
            report = [["test name",
                        "input",
                        "expected output",
                        "real output"]] + self.results
            print toPrettyStringLL(report)

def allTests():
    testingList(Test)
    testingBool(Test)

allTests()






