"""
Author: Nathanael Bayard
Module Name: Error
Description: module used to have a uniform way to raise exceptions.
             In general, i'll prefer reserving the use of exceptions only when something
             went horribly wrong (wrong/absurd type of input, mostly), and using
             Either or Maybe when an operation may fail in a way that "makes sense",
             like an equation system solver that may find the system unsolvable,
             and therefore the space of solutions to be the empty set.
"""

# error : Function . String -> Void [!]
def error(f, report):
    raise Exception('[' + f.func_name + ']:' + str(report))
