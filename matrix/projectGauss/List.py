# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: List
Description: list-related tools.
"""

from Bool import not_

# zippers
def tupled(f):
    def g(tup):
        (x, y) = tup
        return f(*tup)
    return g

def zipWith(f, xs, ys):
    xys = zip(xs, ys)
    return map(tupled(f), xys)

def unzipWith(f, xys):
    xs = []
    ys = []
    for e in xys:
        (x, y) = f(e)
        xs.append(x)
        ys.append(y)
    return (xs, ys)

# filters
def filterOut(f, xs):
    return filter(not_(f), xs)

def subtractLists(xs, ys):
    return filter(lambda e: not e in ys, xs)

def filterOutIx(ixList, l):
    out = []
    for i in range(len(l)):
        e = l[i]
        if i not in ixList:
           out.append(e)
    return out


# accumulators
def count(condition, xs):
    return len(filter(condition, xs))


# searches
def firstIndex(condition, xs):
    for ix in range(len(xs)):
        x = xs[ix]
        if condition(x):
            return ix
    return failure

failure = object()

def notFound(ix):
    return ix == failure


# modificators
def isolateItem(xs, index):
    rest = xs[:index] + xs[index +1 :]
    return (xs[index], rest)

def insert(xs, x, index):
    return xs[:].insert(index, x)

def grouped(xs, size):
    if len(xs) < size:
        return []
    numberOfGroups = len(xs) / int(size)
    return [xs[i:size+i] for i in range(numberOfGroups)]
    
# constructors
def replicate(amount, pattern):
    return [pattern for i in range(amount)]

def strReplicate(amount, pattern):
    return ''.join(replicate(amount, " "))

# lists of lists
def mapLL(f, LL):
    return map(lambda line: map(f, line), LL)

def flatten(LL):
    return reduce(lambda line, line2: line + line2, LL, [])


# pretty printing
def asLines(strL):
    return "\n".join(strL)

def toPrettyString(L):
    toPrettyStringLL([L])

def toPrettyStringLL(LL):
    if LL == []:
        return
    strLL = mapLL(str, LL)
    flattened = flatten(strLL)
    if flattened == []:
        return
    maxLen = max(map(len, flattened))
    colWidth = maxLen + 3
    paddedLL = mapLL(lambda string: padded(string, colWidth), strLL)
    out = []
    for line in paddedLL:
        out.append("".join(line))
    return asLines(out)

def padded(string, desiredSize):
    paddingSize = desiredSize - len(string)
    if paddingSize <= 0:
        return string
    return strReplicate(paddingSize, " ") + string

#LL = [[1, -1, 0.3, Fraction(7,4), "wawaaaaaaa"]]
#prettyPrintLL(LL)
#prettyPrintLL([])