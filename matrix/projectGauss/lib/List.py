# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: List
Description: list/string-related tools.
"""

from Bool import not_
from Maybe import Nothing, Just

# akin to `map : (a -> b) . List a -> List b`
# but the first parameter is a function of two arguments,
# and the list is a list of tuples.
def bimap(f, tupList):
# bimap : (a . b -> c) . List (a, b) -> List c
    out = []
    for tup in tupList:
        out.append(f(*tup))
    return out


# ==== zippers

# zip two lists into a new one, using a function to combine the
# elements of each lists.
def zipWith(f, xs, ys):
# zipWith : (a . b -> c) . List a . List b -> List c
    return bimap(f, zip(xs, ys))

# the reverse operation to zipWith: generates two lists
# from the elements of one list.
def unzipWith(f, xys):
# unzipWith : (a -> (b, c)) . List a -> (List b, List c)
    xs = []
    ys = []
    for e in xys:
        (x, y) = f(e)
        xs.append(x)
        ys.append(y)
    return (xs, ys)

# ==== filters

# like filter in reverse: the elements kept are those that don't
# verify the predicate
def filterOut(f, xs):
# filterOut : (a -> Bool) . List a -> List a
    return filter(not_(f), xs)

# returns the list of the elements of `xs` which aren't in `ys`.
def subtractLists(xs, ys):
# subtractLists : List a . List a -> List a
    return filter(lambda e: not e in ys, xs)

# takes a list of indexes, then a second list
# returns the elements of the second list whose indices
# aren't in the first list
def filterOutIx(ixList, l):
# filterOutIx : List Int . List a -> List a
    out = []
    for i in range(len(l)):
        e = l[i]
        if i not in ixList:
           out.append(e)
    return out


# ==== searches

# returns `Just` the index of the first item for which the
# condition is checked. returns `Nothing` if no item matches
# the condition.
def firstIndex(condition, xs):
# firstIndex : (a -> Bool) . List a -> Maybe Index
    for ix in range(len(xs)):
        x = xs[ix]
        if condition(x):
            return Just(ix)
    return Nothing


# ==== modificators

# small tool to add semantics to tests
# for index-out-of-range related issues.
def outOfRange(index, L):
# outOfRange : Index . List a -> Bool
    return len(L) <= index or index < 0

# takes a list and an index; returns a tuple
# containing the element at the given index,
# and the rest of the elements of the list
# will raise an exception of the index is out of range.
def isolateItem(xs, index):
# isolateItem : List a . Index -> (a, List a)
    if outOfRange(index, L):
        raise Exception()
    rest = xs[:index] + xs[index + 1 :]
    return (xs[index], rest)

# takes a list and a size of groups
# returns a list of lists; each sublist contains `size`
# elements from the original list.
# the final group is discarded if its size is too small.
# e.g.: grouped([1,2,3,4,5,6,7], 2) == [[1,2], [3,4], [5,6]]
#       grouped([1,2,3], 4) == []
def grouped(xs, size):
# grouped : List a . Int -> List (List a)
    numberOfGroups = int(len(xs)) / int(size)
    out = []
    for i in range(numberOfGroups):
        out.append(xs[i*size:(i+1)*size])
    return out
    

# ==== List constructors

# takes an `amount : Int` and a value,
# returns a list of `amount` times the given value.
# e.g.: replicate(3, "foo") == ["foo", "foo", "foo"]
#       replicate(0, "foo") == []
def replicate(amount, pattern):
# replicate : Int . a -> List a
    return [pattern for i in range(amount)]


# ==== lists of lists

# akin to `map` but for lists of lists:
# applies the input function to every subelement
# and returns the resulting new list of lists.
def mapLL(f, LL):
# mapLL : (a -> b) . List (List a) -> List (List b)
    return map(lambda line: map(f, line), LL)

# takes a lists of lists, and fuse each sublist
# into one single "flat" list.
def flatten(LL):
# flatten : List (List a) -> List a
    return reduce(lambda line, line2: line + line2, LL, [])

# ==== pretty printing

# takes a list of values; returns one string with the string
# representation of each value, one per line
# (that is, separated by a newline).
# python not being difficult at the type-level,
# it can be a heterogeneous list in input.
# e.g.: asLines([2, "foo", []]) == "2\nfoo\n[]"
def asLines(L):
# asLines : Line ? -> String
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
