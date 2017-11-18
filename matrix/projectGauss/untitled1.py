# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 06:49:38 2017

@author: nash
"""

from temp import *
import temp

from fractions import Fraction





def combinations(xs, amount):
    if xs == [] or amount == 0:
        return []
    if amount == 1:
        return [[x] for x in xs]
    return [[x] + ys for x in xs for ys in combinations(xs, amount - 1)]
    

def overManyMatrices(do, dim, minVal, maxVal):
    valRange = map(lambda i: Fraction(i), range(minVal, maxVal+1))
    #print valRange, dim, dim*dim
    possibleLeftSides = combinations(valRange, dim*dim)
    possibleRightSides = combinations(valRange, dim)
    count = 0
    for L in possibleLeftSides:
        ML = matrixFromList(L, dim, dim)
        for R in possibleRightSides:    
            #print ML, R
            maybeSol = temp.gaussMethod(ML, R)
            maybeTestRes = maybeSol.maybeApply(testResults, ML, R)
            if not maybeTestRes.isNothing() and maybeTestRes.value != "":
                print "--------------"
                print "one error detected:"
                print maybeTestRes.value
                print "ML =", ML
                print "R =", R
                print "sol =", maybeSol.value
            else:
                count += 1
    #print ML
    print count == len(valRange) ** (dim * (dim + 1))
#overManyMatrices(None, 3, 0, 2)
    
    
        #choices = [[val] for n in range(n) for p in range(p) for val in valRange]
