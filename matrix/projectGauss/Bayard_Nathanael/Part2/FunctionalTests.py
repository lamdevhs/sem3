"""
Author: Nathanael Bayard
Module Name: FunctionalTests
Description: module used for testing that, for trivial systems,
             the algorithm of System.py/systemSolution works.
"""
from List import toPrettyStringLL
from Maybe import Nothing, Just
from Matrix import nullMatrix, idMatrix
from UnitTests import Test


# for testing:
from System import systemSolution

def functionalTests():
    tester = Test(systemSolution)

    idMat = idMatrix(3)
    Y1 = [1,2,3]
    in1 = [idMat, Y1]
    out1 = Just(([], Y1)) # kernel = {0}
    io1 = (in1, out1)
    
    nullMat = nullMatrix(3,3)
    Y2 = [4,5,6]
    in2 = [nullMat, Y2]
    out2 = Nothing # no solution
    io2 = (in2, out2)

    ioList = [io1, io2]
    indices = range(len(ioList))
    for ioIx in zip(ioList, indices):
        ((inp, out), index) = ioIx
        tester.check(input = inp, output = out, testName = "test #" + str(index))
     
    tester.printResults()

functionalTests()






