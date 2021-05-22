import numbers
from functools import singledispatch, wraps


def make_other_expr(meth):
    @wraps(meth)
    def fn(self, other):
        if isinstance(other, numbers.Number):
            other = Number(other)
        return meth(self, other)
    return fn


class Expression:
    def __init__(self, *operands):
        self.operands = operands

    @make_other_expr
    def __add__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        if isinstance(other, Number):
            other = Number(other)
        return Sub(self, other)

    def __mul__(self, other):
        if isinstance(other, Number):
            other = Number(other)
        return Mul(self, other)

    def __truediv__(self, other):
        if isinstance(other, Number):
            other = Number(other)
        return TrueDiv(self, other)

    def __pow__(self, other):
        if isinstance(other, Number):
            other = Number(other)
        return Pow(self, other)


class Operator(Expression):
    def __repr__(self):
        return type(self).__name__ + repr(self.operands)
    
    def __str__(self):