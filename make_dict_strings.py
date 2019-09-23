"""
This solution requires the developer to pass the arguments as a set of strings,
such that each string corresponds to an identifier for a variable in the caller
scope. The callee function then retrieves the variable values from the callee's
stack frame.

> If you quite regularly feel like you need this, then you're quite regularly
> doing something wrong. - Antti Haapala Oct 2 '16 at 17:02
> https://stackoverflow.com/questions/39818733/create-dictionary-where-keys-are-variable-names#comment66929025_39818733
"""

import inspect


def make_dict(*args):
    try:
        caller_frame = inspect.currentframe().f_back
        caller_locals = caller_frame.f_locals
    finally:
        del caller_frame  # https://docs.python.org/3/library/inspect.html#the-interpreter-stack
    return dict(((k, caller_locals[k]) for k in args))

    
"""Test call from function scope"""
def my_func():
    a, b, c, d = 1, 2, 3, 4
    e, f, g, h = 4, 5, 6, 7
    print make_dict('a', 'b', 'c', 'd')
    
my_func()

"""Test call from global scope
a,b,c,d=1,2,3,4
print make_dict('a','b','c','d')
"""