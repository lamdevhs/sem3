from List import zipWith
from List import toPrettyStringLL


class Test():
    def __init__(self, functionToTest):
        self.toTest = functionToTest
        self.name = functionToTest.func_name
        self.results = []
    
    def check(self, input, expectedOutput, testName = "untitled test"):
        actualOutput = self.toTest(*input)
        if actualOutput != expectedOutput:
            self.results.append([testName, input, expectedOutput, actualOutput])
        return self

    def printResults(self):
        print 'unit test for function "' + self.name + '":',
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
    # zipWith :: (a . b -> c) . [a] . [b] -> [c]
    def f(a, b):
        return a + b
    Test(zipWith
        ).check( [f, [1,2,3], [4,5,6]], [5,7,9], "addition"
        ).check( [f, [], []], [], "empty"
        ).printResults()

allTests()