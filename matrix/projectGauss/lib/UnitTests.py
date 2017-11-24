from List import zipWith, unzipWith, filterOut, subtractLists
from List import toPrettyStringLL


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
    # zipWith :: (a . b -> c) . List a . List b -> List c
    def f(a, b):
        return a + b
    Test(zipWith
        ).check( input = [f, [1,2,3], [4,5,6]],
                 output = [5,7,9],
                 testName = "addition"
        ).check( input = [f, [], []],
                 output = [],
                 testName = "empty lists"
        ).check( input = (f, [10], [1,2,3]),
                 output = [11],
                 testName = "lists of different sizes"
        ).printResults()

    # unzipWith :: (a -> (b, c)) . List a -> (List b, List c)
    def f(a):
        return (a[:1], a[1:])
    Test(unzipWith
        ).check( input = (f, ["abc", "tree", "bird"]),
                 output = (["a", "t", "b"], ["bc", "ree", "ird"]),
                 testName = "beheading"
        ).check( input = [f, []],
                 output = ([], []),
                 testName = "empty lists"
        ).printResults()

    # filterOut :: (a -> Bool) . List a -> List a
    def f(x):
        return x % 2 == 0
    Test(filterOut
        ).check( input = (f, [1,2,3,4,5,6]),
                 output = [1,3,5],
                 testName = "remove pairs"
        ).check( input = (f, []),
                 output = [],
                 testName = "empty list"
        ).printResults()
    
    # subtractLists :: List a . List a -> List a
    Test(subtractLists
        ).check( input = ([1,2,3], [2,3]),
                 output = [1],
                 testName = "subtract"
        ).check( input = ([1,2,3], [1,2,3]),
                 output = [],
                 testName = "subtract itself"
        ).check( input = ([7,8,9], [1,2,3,4,5,6]),
                 output = [7,8,9],
                 testName = "disjoint lists"
        ).check( input = ([1,2,3], []),
                 output = [1,2,3],
                 testName = "subtract empty list"
        ).printResults()

    # filterOutIx :: List Integer . List a -> List a
    Test(filterOutIx
        ).check( input = ([1,2,3], ["a", "b", "c", "d", "e"]),
                 output = ["a", "e"],
                 testName = "1 to 3"
        ).check( input = ([], [1,2,3,4,5]),
                 output = [1,2,3,4,5],
                 testName = "ix list empty"
        ).check( input = ([7,8,9], [1,2,3,4,5,6]),
                 output = [7,8,9],
                 testName = "disjoint lists"
        ).check( input = ([1,2,3], []),
                 output = [1,2,3],
                 testName = "subtract empty list"
        ).printResults()

allTests()
