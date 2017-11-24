# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: List
Description: list/string-related tools.
"""

from Bool import not_

# bimap : (a . b -> c) . List (a, b) -> List c
def bimap(f, tupList):
    out = []
    for tup in tupList:
        out.append(f(*tup))
    return out

# zippers
#def tupled(f):
#    def g(tup):
#        (x, y) = tup
#        return f(*tup)
#    return g

def zipWith(f, xs, ys):
    return bimap(f, zip(xs, ys))

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


## accumulators
#def count(condition, xs):
#    return len(filter(condition, xs))


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

#def insert(xs, x, index):
#    return xs[:].insert(index, x)

def grouped(xs, size):
    if len(xs) < size:
        return []
    numberOfGroups = int(len(xs)) / int(size)
    out = []
    for i in range(numberOfGroups):
        out.append(xs[i*size:(i+1)*size])
    return out
    
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
def asLines(L):
    return "\n".join(map(str, L))

#     if len(strL) == 0:
#         return ""
#     if len(strL) == 1:
#         return strL[0]
#     out = strL[0]
#     rest = strL[1:]
#     for s in rest:
#         out += "\n" + s
#     return out

def asWords(L):
    return " ".join(map(str, L))

def toPrettyString(L):
    return toPrettyStringLL([L])

def toPrettyStringLL(LL):
    if LL == []:
        return ""
        
    strLL = mapLL(toStr, LL)
    flattened = flatten(strLL)
    if flattened == []:
        return ""
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



def dummy_func():
    pass
functionClass = dummy_func.__class__

dummy_list = []
listClass = dummy_list.__class__
dummy_tuple = (1,2,3)
tupleClass = dummy_tuple.__class__

def toStr(x):
    return str(funcToStr(x))

def funcToStr(x):
    if x.__class__ == functionClass:
        return "<" + x.func_name + ">"
    elif x.__class__ == listClass or x.__class__ == tupleClass:
        return map(funcToStr, x)
    else:
        return x

#LL = [[1, -1, 0.3, Fraction(7,4), "wawaaaaaaa"]]
#prettyPrintLL(LL)
#prettyPrintLL([])
