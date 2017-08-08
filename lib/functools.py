import util
import functools


@functools.total_ordering
class Value:
    """ The class must define one of __lt__(), __le__(), __gt__(), or __ge__(). In addition, the class should supply an __eq__() method.
     all the other comparison function will be automatically implimented
     """

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """ define == """
        return self.value == other.value

    def __lt__(self, other):
        """ define < """
        return self.value < other.value


class TestTotalOrdering(util.TestCaseBase):
    """ """
    def test(self):
        """ test > """
        v1 = Value(1)
        v2 = Value(2)
        self.assertTrue(v2 > v1)


