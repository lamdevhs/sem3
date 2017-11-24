# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: Maybe
Description: type to represent potentially erroneous values. does not support error report messages.
"""

class Maybe():
    def __init__(self, value):
        self.value = value

    def isNothing(self):
        return self == Nothing
    
    def maybeDo(self, f, *args):
        if self.isNothing():
            return self
        else:
            return f(self.value, *args)

    def maybeApply(self, f, *args):
        if self.isNothing():
            return self
        else:
            return Just(f(self.value, *args))

Nothing = Maybe(object())

def Just(x):
    return Maybe(x)