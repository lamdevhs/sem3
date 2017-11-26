# from UnitTests import Test

# for testing:
from List import *

# the class Test from UnitTests.py
# is given in parameters to prevent cycling dependency
# between both modules
def testingList(Test):
    print "==== unit tests for List.py:"

    # bimap : (a . b -> c) . List (a, b) -> List c
    def f(a, b):
        return a + b
    Test(bimap
        ).check( input = (f, [(1,2), (3,4), (5,6)]),
                 output = [3,7,11],
                 testName = "addition"
        ).check( input = (f, []),
                 output = [],
                 testName = "empty lists"
        ).printResults()

    # zipWith : (a . b -> c) . List a . List b -> List c
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

    # unzipWith : (a -> (b, c)) . List a -> (List b, List c)
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

    # filterOut : (a -> Bool) . List a -> List a
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
    
    # subtractLists : List a . List a -> List a
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

    # filterOutIx : List Index . List a -> List a
    Test(filterOutIx
        ).check( input = ([1,2,3], ["a", "b", "c", "d", "e"]),
                 output = ["a", "e"],
                 testName = "1 to 3"
        ).check( input = ([], [1,2,3,4,5]),
                 output = [1,2,3,4,5],
                 testName = "ix list empty"
        ).check( input = ([7,8,9], [1,2]),
                 output = [1,2],
                 testName = "incorrect indexes"
        ).check( input = ([1,2,3], []),
                 output = [],
                 testName = "empty list"
        ).printResults()
    
    # firstIndex : (a -> Bool) . List a -> Maybe Index
    def f(i):
        return i >= 3
    Test(firstIndex
        ).check( input = (f, [0,1,2,3,4,5,6]),
                 output = Just(3),
                 testName = "val >= 3"
        ).check( input = (f, []),
                 output = Nothing,
                 testName = "emptyList"
        ).check( input = (f, [0,1,2]),
                 output = Nothing,
                 testName = "emptyList"
        ).printResults()
      
    # outOfRange : Index . List a -> Bool
    Test(outOfRange
        ).check( input = (0, [0,1,2,3,4,5,6]),
                 output = False,
                 testName = "not out of range"
        ).check( input = (2, [0,1]),
                 output = True,
                 testName = "out of range"
        ).check( input = (1, []),
                 output = True,
                 testName = "emptyList"
        ).check( input = (-2, []),
                 output = True,
                 testName = "negativeIndex"
        ).printResults()
    

    # isolateItem : List a . Index -> (a, List a)
    Test(isolateItem
        ).check( input = ([2,3,4,5,6], 1),
                 output = (3, [2,4,5,6]),
                 testName = "not out of range"
        ).checkError( input = ([0,1], 2),
                      testName = "out of range"
        ).checkError( input = ([], 1),
                      testName = "emptyList"
        ).checkError( input = ([], -2),
                      testName = "negativeIndex"
        ).printResults()

    # grouped : List a . Int -> List (List a)
    Test(grouped
        ).check( input = ([1,2,3,4], 2),
                 output = [[1,2],[3,4]],
                 testName = "pair of pairs"
        ).check( input = ([1,2,3,4, 5], 2),
                 output = [[1,2],[3,4]],
                 testName = "truncation"
        ).check( input = ([1,2,3], 1),
                 output = [[1],[2],[3]],
                 testName = "each alone"
        ).check( input = ([1,2,3], 5),
                 output = [],
                 testName = "too big"
        ).checkError( input = ([1,2,3], 0),
                      testName = "null amount"
        ).checkError( input = ([1,2,3], -2),
                      testName = "negative amount"
        ).printResults()
        
    # replicate : Int . a -> List a
    Test(replicate
        ).check( input = (3, 0),
                 output = [0,0,0],
                 testName = "three times nothing"
        ).check( input = (0, 0),
                 output = [],
                 testName = "zero times nothing"
        ).check( input = (-1, 0),
                 output = [],
                 testName = "less than nothing"
        ).printResults()
       
    # strReplicate : Int . String -> String
    Test(strReplicate
        ).check( input = (3, "z"),
                 output = "zzz",
                 testName = "zzz"
        ).check( input = (0, 'z'),
                 output = "",
                 testName = "zero z's"
        ).check( input = (-1, 'z'),
                 output = "",
                 testName = "less than z"
        ).printResults()

    # mapLL : (a -> b) . List (List a) -> List (List b)
    def f(x):
        return x + 42
    Test(mapLL
        ).check( input = (f, []),
                 output = [],
                 testName = "empty"
        ).check( input = (f, [[], []]),
                 output = [[], []],
                 testName = "lists of empty lists"
        ).check( input = (f, [[1,2],[3]]),
                 output = [[43, 44], [45]],
                 testName = "typical usage"
        ).printResults()


    # warning: in several of the following tests the input is always one single list
    # and since `Test.check` expects a list/tuple of arguments, i have
    # to enclose the one input into another list (python does not allow tuples of one element).
    # eg: `input = [[1]]` does not represent an input of type `List (List Num)`
    # but in fact represents the list of the arguments, with the first and only
    # argument being a list `List Num`.


    # flatten : List (List a) -> List a
    Test(flatten
        ).checkError( input = [[1,2,3,4]],
                 testName = "flatten an already flat list"
        ).check( input = [[[1], [2, 0], [3]]],
                 output = [1,2,0,3],
                 testName = "typical usage"
        ).check( input = [[]],
                 output = [],
                 testName = "empty list"
        ).printResults()

    # asLines : List a -> String
    Test(asLines
        ).check( input = [["a", [], 1]],
                 output = "a\n[]\n1",
                 testName = "asLines 1"
        ).check( input = [[]],
                 output = "",
                 testName = "empty input list"
        ).printResults()
    # asWords : List a -> String
    Test(asWords
        ).check( input = [["a", [], 1]],
                 output = "a [] 1",
                 testName = "asWords 1"
        ).check( input = [[]],
                 output = "",
                 testName = "empty input list"
        ).printResults()

    # concatStrings : List a -> String
    Test(concatStrings
        ).check( input = [["a", [], 1]],
                 output = "a[]1",
                 testName = "concatStrings 1"
        ).check( input = [[]],
                 output = "",
                 testName = "empty input list"
        ).printResults()

    # toPrettyString : Line a -> String
    Test(toPrettyString
        ).check( input = [[]],
                 output = "",
                 testName = "empty list"
        ).check( input = [["", 1,12,123]],
                 output = "           1    12   123",
                 testName = "1, 12, 123!"
        ).printResults()





