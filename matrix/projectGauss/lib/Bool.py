# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: Bool
Description: tools relative to boolean values and predicates
"""

    
# wrappers for mapping
def andBool(b, c):
    return b and c

def orBool(b, c):
    return b or c

# extension of predicate to lists:
def forall(l, condition):
    for e in l:
        if not condition(e): return False
    return True

def forany(l, condition):
    for e in l:
        if condition(e):
            return True
    return False



# predicate combinators
#def allTrue(*args):
#    def f(x):
#        return reduce(andBool, map(lambda f: f(x), args), True)
#    return f

def anyTrue(*args):
    def f(x):
        return reduce(orBool, map(lambda f: f(x), args), False)
    return f

#def noneTrue(*args):
#    return not_(anyTrue(*args))

def not_(boolFn):
    def negation(*args):
        return not boolFn(*args)
    return negation
    
# basic predicates
def isNotZero(value):
    return value != 0

def isZero(value):
   return value == 0 



