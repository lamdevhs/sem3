"""
Author: Nathanael Bayard
Module Name: Maybe
Description: type to represent potentially erroneous values. does not support error report messages.
"""

#   type Maybe t = Nothing | Just t
# /
# Two types of values which can have type `Maybe t`:
# /
#  Nothing : Maybe t
#  Just(x) : Maybe t
# /
# With `x : t` of course
# Nothing is not a function, it's a unique dummy value
# (which in a typed language could have different types depending on circumstances)
class Maybe():

    # this constructor is not meant to be called directly.
    # below the Maybe class are the two proper ways to get
    # a value of type `Maybe t`: Nothing and Just
    def __init__(self, value):
        self._value = value

    
    # returns the inner value `x` if the input is `Just(x)`
    # raises an error if the input is `Nothing`
    # 
    #   justValue : Maybe t -> t [!]
    def justValue(self):
        if self == Nothing:
            error(justValue, "Nothing has no inner value")
        else:
            return self._value

    # cf PDF for more in-depth explanation
    # takes the result of a previous operation, and if it's an error,
    # just outputs Nothing, else, returns the result of a new operation,
    # which can itself be Nothing, or not.
    #
    # axiomatically:
    # /
    #   Nothing.maybeDo(f, other_args) == Nothing
    #   Just(x).maybeDo(f, other_args) == f(x, other_args)
    # /
    # with `f(x, other_args) : Maybe b`
    # and so esp we can have `f(x, other_args) == Nothing`
    # aka f can fail too.
    #
    # so, putting aside the variadic stuff (only necessary because
    # python does not allow arbitrary currying of functions)
    # /
    #   maybeDo : Maybe a . (a -> Maybe b) -> Maybe b
    def maybeDo(self, f, *args):
        if self == Nothing:
            return self
        else:
            return f(self._value, *args)

    # cf PDF for more in-depth explanation
    # from "mabye a result" of a previous operation, and a function `f`,
    # returns `Nothing` if the input is `Nothing`,
    # or returns `Just` a new non-erroneous result being the output of the function `f`
    # applied to the previous operation's, result content.
    #
    # axiomatically:
    # /
    #   Nothing.maybeApply(f, other_args) == Nothing
    #   Just(x).maybeApply(f, other_args) == Just(f(x, other_args))
    # /
    # with `f(x, other_args)` a function of type `b`
    # so, putting aside the variadic stuff:
    # /
    #   maybeApply : Maybe a . (a -> b) -> Maybe b
    def maybeApply(self, f, *args):
        if self == Nothing:
            return self
        else:
            return Just(f(self._value, *args))
    
    # definition of equality between values of type `Maybe t`
    # useful for UnitTest.py (and to define Nothing in a more precise manner)
    # axiomatically:
    # /
    #   Nothing != Just(x)
    #   Nothing == Nothing
    #   Just(x) == Just(y) ssi x == y
    # /
    #   (==) : Maybe t . Maybe t -> Bool
    def __eq__(self, other):
        return self._value == other._value

    # for some absurd reason, python doesn't have this behavior as default
    # without it, we'd end up with 
    # `Just(3) == Just(3)` and `Just(3) != Just(3)` both true.
    # the use of (==) in `__ne__` directly triggers the call to `__eq__`
    # above.
    # /
    #   (!=) : Maybe t . Maybe t -> Bool
    def __ne__(self, other):
        return not self == other

    # make a string out of `Maybe t` values; mostly used for the sake of UnitTest.py
    def __repr__(self):
        if self == Nothing:
            return "Nothing"
        return "Just " + str(self.value)

# Nothing : Maybe t
Nothing = Maybe(object())

# Just : t -> Maybe t
def Just(x):
    return Maybe(x)

# maps a function `f` which may fail (return Nothing)
# over a list `xs`. returns Nothing if one call to `f`
# results in `Nothing`, returns `Just` the result of
# the mapping otherwise.
#
#   maybeMap : (a -> Maybe b) . List a -> Maybe (List b)
def maybeMap(f, xs)
    out = []
    for x in xs:
        y = f(x)
        if y == Nothing:
            return y
        else:
            out.append(y.justValue())
    return Just(out)
