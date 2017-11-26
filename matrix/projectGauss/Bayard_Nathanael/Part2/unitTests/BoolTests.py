# from UnitTests import Test

# for testing:
from Bool import *


# not all of them are tested because some are just wrapping trivial built-in operators

# the class Test from UnitTests.py
# is given in parameters to prevent cycling dependency
# between both modules
def testingBool(Test):
    print "==== unit tests for Bool.py:"

    # forall : List a . (a -> Bool) -> Bool
    Test(forall
        ).check( input = ([1,2,3,4], isNotZero),
                 output = True,
                 testName = "yes forall"
        ).check( input = ([], isNotZero),
                 output = True,
                 testName = "empty list"
        ).check( input = ([0,1,2,0], isZero),
                 output = False,
                 testName = "not forall"
        ).printResults()

    # anyTrue : List (a -> Bool) -> (a -> Bool)
    pairOr13 = anyTrue(lambda x: x % 2 == 0, lambda x: x == 13)
    pairOr13.func_name = "anyTrue"
        # ^ for the sake of the report that will be printed by Test.printResults

    Test(pairOr13
        ).check( input = [13],
                 output = True,
                 testName = "yes is13"
        ).check( input = [2],
                 output = True,
                 testName = "yes pair"
        ).check( input = [1],
                 output = False,
                 testName = "neither pair nor 13"
        ).printResults()

    # not_ : (a -> Bool) -> (a -> Bool)
    notPairNor13 = not_(pairOr13)
    notPairNor13.func_name = "not_"
        # ^ for the sake of the report that will be printed by Test.printResults

    Test(notPairNor13
        ).check( input = [1],
                 output = True,
                 testName = "yes 1"
        ).check( input = [2],
                 output = False,
                 testName = "no bc pair"
        ).check( input = [13],
                 output = False,
                 testName = "no bc 13"
        ).printResults()
