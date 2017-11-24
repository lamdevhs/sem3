# -*- coding: utf-8 -*-
"""
Author: Nathanael Bayard
Module Name: Either
Description: type to represent potentially erroneous values, with an error message.
"""

class Either():
    def __init__(self, value, isLeft = False):
        if isLeft:
            self.leftValue = value
        else:
            self.rightValue = value
        self.isLeft = isLeft
        self.isRight = not isLeft
    def eitherDo(self, f, *args):
        if self.isLeft:
            return self
        else:
            return f(self.rightValue, *args)
    def eitherApply(self, f, *args):
        if self.isLeft:
            return self
        else:
            return Right(f(self.rightValue, *args))

def Right(value):
    return Either(value, isLeft = False)

def Left(value):
    return Either(value, isLeft = True)


def eitherSequence(f, xs):
    out = []
    for x in xs:
        y = f(x)
        if y.isLeft:
            return y
        else:
            out.append(y.rightValue)
    return Right(out)