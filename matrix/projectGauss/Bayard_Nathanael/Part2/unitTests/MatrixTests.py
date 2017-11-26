from Maybe import Just, Nothing

# for testing:
from Matrix import *


# the class Test from UnitTests.py
# is given in parameters to prevent cycling dependency
# between both modules
def testingMatrix(Test):
    print "==== unit tests for Matrix.py:"

    # checkDim : Int -> Void
    Test(checkDim
        ).checkError( input = [0], testName = "dim = 0"
        ).checkError( input = [-1], testName = "dim = -1"
        ).printResults()
    
    # checkIx : Int . Int -> Void
    Test(checkIx
        ).checkError( input = [0, 0], testName = "0,0"
        ).checkError( input = [-1, 5], testName = "-1,5"
        ).printResults()

    # nullVector : [Num n] Dim -> Vector n
    Test(nullVector
        ).check( input = [3], output = [0,0,0], testName = "dim = 0"
        ).printResults()

    # nullMatrix : [Num n] Dim . Dim -> Matrix n
    Test(nullMatrix
        ).check( input = [3, 2], output = [[0,0],[0,0], [0,0]], testName = "n,p = 3,2"
        ).printResults()

    # unitVector : [Num n] Int . Int -> Vector n
    Test(unitVector
        ).check( input = [4,2], output = [0,0,1,0], testName = "e2 from R4"
        ).printResults()

    # idMatrix : [Num n] Int -> Matrix n
    Test(idMatrix
        ).check( input = [3], output = [[1,0,0],[0,1,0],[0,0,1]], testName = "Id3"
        ).printResults()

    # matrixFromList : [Num n] List n . Int . Int -> Matrix n
    Test(matrixFromList
        ).checkError( input = ([1,2,3], 2,2), testName = "wrong list length"
        ).check( input = ([1,2,3,4,5,6], 3,2), output = [[1,2],[3,4],[5,6]], testName = "some matrix"
        ).printResults()

    # listFromMatrix : [Num n] Matrix n -> List n
    Test(listFromMatrix
        ).check( input = [[[1, 0],[2, 0],[3, 0]]], output = [1,0,2,0,3,0], testName = "some matrix"
        ).printResults()

    # ncols : [Num n] Matrix n -> Int
    Test(ncols
        ).checkError( input = [[1,2]], testName = "a list, not a matrix"
        ).check( input = [[[1, 0],[2, 0],[3, 0]]], output = 2, testName = "some matrix"
        ).printResults()

    # nrows : [Num n] Matrix n -> Int
    Test(nrows
        ).check( input = [[[1, 0],[2, 0],[3, 0]]], output = 3, testName = "some matrix"
        ).printResults()

    # isNullVector : [Num n] Vector n -> Bool
    Test(isNullVector
        ).check( input = [[0,0,0,0]], output = True, testName = "yes null"
        ).check( input = [[0,0,0,1]], output = False, testName = "not null"
        ).printResults()

    # isNullMatrix : [Num n] Matrix n -> Bool
    Test(isNullMatrix
        ).check( input = [[[0, 0],[0, 0],[0, 0]]], output = True, testName = "yes null"
        ).check( input = [[[0, 0],[0, 0],[1, 0]]], output = False, testName = "not null"
        ).printResults()

    # firstNonNullEachLine : [Num n] Matrix n -> Maybe (List Index)
    Test(firstNonNullEachLine
        ).check( input = [[[0, 1],[0, 0],[0, 0]]], output = Nothing, testName = "one line is null"
        ).check( input = [[[0, 1],[1, 0],[1, 0]]], output = Just([1,0,0]), testName = "foo...fooo"
        ).printResults()

    # columnAt : Index . Matrix t ->  Column t
    Test(columnAt
        ).check( input = [0, [[1, 0],[2, 0],[3, 0]]], output = [1,2,3], testName = "some matrix"
        ).check( input = [1, [[1, 0],[2, 0],[3, 0]]], output = [0,0,0], testName = "some matrix"
        ).checkError( input = [2, [[1, 0],[2, 0],[3, 0]]], testName = "wrong index"
        ).printResults()

    # transposed : Matrix t -> Matrix t
    Test(transposed
        ).check( input = [[[1, 0],[2, 0],[3, 0]]], output = [[1,2,3],[0,0,0]], testName = "some matrix"
        ).printResults()

    # negate : [Num n] Matrix n -> Matrix n
    Test(negate
        ).check( input = [[[1, 0],[2, 0],[3, 0]]], output = [[-1, 0],[-2, 0],[-3, 0]], testName = "some matrix"
        ).printResults()

    # mapMatrix : (a -> b) . Matrix a -> Matrix b
    def add42(x):
        return x + 42
    Test(mapMatrix
        ).check( input = (add42, [[100, 0],[200, 0],[300, 0]]), output = [[142, 42],[242, 42],[342, 42]],
                 testName = "42 forever!"
        ).printResults()
