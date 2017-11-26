"""
Author: Nathanael Bayard
Module Name: List
Description: list/string-related tools.
"""

from Bool import not_
from Maybe import Nothing, Just
from Error import error

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

# returns the index of the first
# element that matches the predicate
def firstIndex(condition, xs):
# firstIndex : (a -> Bool) . List a -> Maybe Index
    for ix in range(len(xs)):
        x = xs[ix]
        if condition(x):
            return Just(ix)
    return Nothing


# ==== modificators

def outOfRange(index, L):
# outOfRange : Index . List a -> Bool
    return len(L) <= index or index < 0

# takes a list and an index; returns a tuple
# containing the element at the given index,
# and the rest of the elements of the list
# will raise an exception of the index is out of range.
def isolateItem(xs, index):
# isolateItem : List a . Index -> (a, List a)
    if outOfRange(index, xs):
        error(isolateItem, "out of range index")
    rest = xs[:index] + xs[index + 1 :]
    return (xs[index], rest)

# takes a list and a size of group
# returns a list of lists; each sublist contains `size`
# elements from the original list.
# the final group is discarded if its size is too small.
# e.g.: grouped([1,2,3,4,5,6,7], 2) == [[1,2], [3,4], [5,6]]
#       grouped([1,2,3], 4) == []
def grouped(xs, size):
# grouped : List a . Int -> List (List a)
    if size <= 0:
        error(grouped, "group size must be non nul natural integer")
    numberOfGroups = int(len(xs)) / int(size)
    out = []
    for i in range(numberOfGroups):
        out.append(xs[i*size:(i+1)*size])
    return out
    

# ==== List constructors

# e.g.: replicate(3, "foo") == ["foo", "foo", "foo"]
#       replicate(0, "foo") == []
#       replicate(-1, "foo") == []
def replicate(amount, pattern):
# replicate : Int . a -> List a
    return [pattern for i in range(amount)]

def strReplicate(amount, pattern):
# strReplicate : Int . String -> String
    if amount <= 0:
        return ''
    return pattern + strReplicate(amount - 1, pattern)

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

# e.g.: asLines([4, [], "foo"]) == "4\n[]\nfoo"
def asLines(L):
# asLines : List a -> String
    return "\n".join(map(str, L))

# e.g.: asWords([4, [], "foo"]) == "4 [] foo"
def asWords(L):
# asWords : List a -> String
    return " ".join(map(str, L))

def concatStrings(L):
# concatStrings : List a -> String
    return "".join(map(str, L))

# function to print a list of lists of values
# as an array with constant-sized columns
def toPrettyStringLL(LL):
# toPrettyStringLL : List a -> String
    if LL == []:
        return ""
        
    # i use `toStr` (written below) instead of the built-in
    # `str` because i want to be able to print
    # lists of lists containing functions (cf UnitTest.py)
    # and by default str(f) would write something like
    # '<function f at 0x7f510ce826e0>'
    # which is ugly and verbose
    strLL = mapLL(toStr, LL)
    
    flattened = flatten(strLL) # flattened so i can use max below
    if flattened == []:
        return ""
    
    maxLen = max(map(len, flattened))
    constantWidth = maxLen + 3
    
    # i add some custom padding to each value of strLL
    # so they each have the same constantWidth
    paddedLL = mapLL(lambda string: padded(string, constantWidth), strLL)
   
    # fuse the elements of each sublist
    lines = map(concatStrings, paddedLL)
    
    # fuse the sublists with \n
    return asLines(lines)

# completes a string with space to its left so its length
# matches a desired value
def padded(string, desiredLength):
    paddingSize = desiredLength - len(string)
    if paddingSize <= 0:
        return string
    return strReplicate(paddingSize, " ") + string

def toPrettyString(L):
# toPrettyString : Line a -> String
    return toPrettyStringLL([L])



# all that follows, up to the definition of `toStr`
# is used to check the type of objects

def dummy_func():
    pass
dummy_tuple = (1,2,3) # for some reason python calls "tuple" any n-uple of whichever size `n`
dummy_list = []

listClass = dummy_list.__class__
functionClass = dummy_func.__class__
tupleClass = dummy_tuple.__class__

# toStr : a -> String
def toStr(x):
    # recursively uses `funcToStr` to replace
    # functions with their __name__ attribute
    # (which is a string) then use the built-in
    # `str` over the result as per usual.
    return str(funcToStr(x))

# this function's type is vaguely complex, since it literally
# depends on its input values (aka it pertains to type dependency)
def funcToStr(x):
    if x.__class__ == functionClass:
        return "<" + x.func_name + ">"
    elif x.__class__ == listClass or x.__class__ == tupleClass:
        return map(funcToStr, x)
    else:
        return x
