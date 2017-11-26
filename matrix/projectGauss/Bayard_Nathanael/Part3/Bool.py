"""
Author: Nathanael Bayard
Module Name: Bool
Description: tools relative to boolean values and predicates
"""

    
# ==== wrappers of built-in operators for mapping

# orBool : Bool . Bool -> Bool
def orBool(b, c):
    return b or c

# ==== extension of predicate to lists:

# as per math principles, forall over an empty list
# is always true.
#
# forall : List a . (a -> Bool) -> Bool
def forall(l, condition):
    for e in l:
        if not condition(e):
            return False
    return True

# as per math principles, forall over an empty list
# is always False.
#
#   forany : List a . (a -> Bool) -> Bool
def forany(l, condition):
    for e in l:
        if condition(e):
            return True
    return False



# ==== predicate combinators

# takes a list of predicates
# returns a predicate which is true when at least one of them
# is true. takes advantage of python's variadic style
# so we don't need to write the list of predicates between square
# brackets: `anyTrue(pred1, pred2, pred3) : a -> Bool`
# anyTrue : List (a -> Bool) -> (a -> Bool)
def anyTrue(*args):
    def f(x):
        return reduce(orBool, map(lambda f: f(x), args), False)
    return f

# not_ : (a -> Bool) -> (a -> Bool)
def not_(boolFn):
    def negation(*args):
        return not boolFn(*args)
    return negation
    
# ==== basic predicates, just to add semantics to the code

# isNotZero : [Num n] n -> Bool
def isNotZero(value):
    return value != 0

# isZero : [Num n] n -> Bool
def isZero(value):
   return value == 0 

