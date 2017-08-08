class MyNumberUnaryOperator(object):
    """ unary operator """

    def __pos__(self):
        """ + 1 """

    def __neg__(self):
        """ - 1 """

    def __abs__(self):
        """ abs() """

    def __invert__(self):
        """ ~ 1 """

    def __round__(self, n=None):
        """ round() """

    def __floor__(self):
        """ math.floor() """

    def __ceil__(self):
        """ math.ceil() """

    def __trunc__(self):
        """ math.trunc() """


class MyNumberNormalArithmeticOperator(object):
    """ normal arithmetic operators  """

    def __add__(self, other):
        """ 1 + 2 """

    def __sub__(self, other):
        """ 1 - 2 """

    def __mul__(self, other):
        """ 1 * 2 """

    def __floordiv__(self, other):
        """ 1 // 2 """

    def __div__(self):
        """ 1/ 2 """

    def __truediv__(self, other):
        """ 1 /2  when __future__ import division"""

    def __mod__(self, other):
        """ 1 % 2 """

    def __divmod__(self, other):
        """ divmod()  returns quotient and remainder """

    def __pow__(self, power, modulo=None):
        """ 1 ** 2"""

    def __lshift__(self, other):
        """ 1 << 2"""

    def __rshift__(self, other):
        """ 1 >> 2 """

    def __and__(self, other):
        """ 1 & 2 """

    def __or__(self, other):
        """ 1 | 2 """

    def __xor__(self, other):
        """ 1 ^ 2 """


class MyNumberReflectedArithmeticOperator(object):
    """ reflected arithmetic  operators """

    def __radd__(self, other):
        """ noninstance + instance : only get called when the right value is not an instance of the class
         1 + MyNumber will call __radd__
         MyNumber + i will call __add__
         """

    def __rsub__(self, other):
        """ 1 - MyNumber """

    def __rmul__(self, other):
        """ 1 *  MyNumber"""

    def __rfloordiv__(self, other):
        """ 1 // MyNumber """

    def __rdiv__(self):
        """ 1/ MyNumber """

    def __rtruediv__(self, other):
        """ 1 / MyNumber  when __future__ import division"""

    def __rmod__(self, other):
        """ 1 % MyNumber """

    def __rdivmod__(self, other):
        """ divmod()  returns quotient and remainder """

    def __rpow__(self, power, modulo=None):
        """ 1 ** MyNumber"""

    def __rlshift__(self, other):
        """ 1 << MyNumber"""

    def __rrshift__(self, other):
        """ 1 >> MyNumber """

    def __rand__(self, other):
        """ 1 & MyNumber """

    def __ror__(self, other):
        """ 1 | MyNumber """

    def __rxor__(self, other):
        """ 1 ^ MyNumber """


class MyNumberAugmentedAssignment(object):
    """  augment assignment """
    def __iadd__(self, other):
        """ x+= 1 """


class TypeConversion(object):
    """ """
    def __int__(self):
        """ int(X) """

    def __long__(self):
        """ long(x) """

    def __float__(self):
        """ float(x) """

    def __complex__(self):
        """ flloat(x) """

    def __oct__(self):
        """ oct(x)"""

    def __hex__(self):
        """ hex(x) """

    def __index__(self):
        """ a[x]"""

    def __trunc__(self):
        """ ??? """

    def __coerce__(self, other):
        """ ??? """

